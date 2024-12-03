import time
from datetime import datetime
from fastapi import APIRouter, Form, HTTPException, UploadFile
from fastapi.responses import UJSONResponse

route = APIRouter()



@route.get('/ping')
async def ping():
    
    time_n = datetime.fromtimestamp(time.time())
    time_now = time_n.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    
    server_info = {
        "message": "ping test",
        "applicationName": "odapi-compare",
        "version": "v1.0.0",
        "serverTime": time_now
    }
    
    return server_info


@route.post('/similarity', response_class=UJSONResponse)
async def  similarity(
    original_file: UploadFile = Form(), compare_file: UploadFile = Form()
):
    """
    Route that receives as input parameter an image and detects text from it.

    :param original_file: Represents the old image that must be replaced with compare_file
    :param compare_file: Represents the file that must be compared with original
    :return: JSON with "similar: yes/no"
    """
    response = {}

    LOG.info(
        '[IN] Input images ["%s", "%s"]',
        original_file.filename,
        compare_file.filename,
    )
    try:
        original_file_contents = original_file.file.read()
        compare_file_contents = compare_file.file.read()
    except Exception as e:
        LOG.error(e)
        raise HTTPException(
            status_code=500, detail="Something gone wrong. Exception was raised."
        ) from e

    if len(original_file_contents) == 0 or len(compare_file_contents) == 0:
        LOG.error(constants.ERROR_DESC["303"])
        raise UnicornException(code=303, msg=constants.ERROR_DESC["303"])

    mime_type_original = magic.from_buffer(original_file_contents, mime=True)
    mime_type_compare = magic.from_buffer(compare_file_contents, mime=True)
    if (
        mime_type_original not in constants.IMAGE_ALLOWED_CONTENT_TYPES
        or mime_type_compare not in constants.IMAGE_ALLOWED_CONTENT_TYPES
    ):
        LOG.error(constants.ERROR_DESC["311"])
        raise UnicornException(code=311, msg=constants.ERROR_DESC["311"])

    original_image = cv2.imdecode(
        np.frombuffer(original_file_contents, np.uint8), cv2.IMREAD_GRAYSCALE
    )
    compare_image = cv2.imdecode(
        np.frombuffer(compare_file_contents, np.uint8), cv2.IMREAD_GRAYSCALE
    )

    LOG.info(
        "%s was decoded with sizes %s=(h, w, c) and %s with sizes %s=(h, w, c)",
        original_file.filename,
        original_image.shape,
        compare_file.filename,
        compare_image.shape,
    )
    time.sleep(2)

    try:
        is_match = feature_matching(
            original_image,
            compare_image,
            CONFIG.params["SIFT"]["RatioThreshold"],
            CONFIG.params["SIFT"]["MatchThreshold"],
        )
    except Exception as e:
        LOG.error(e)
        LOG.error(traceback.format_exc())
        raise HTTPException(
            status_code=500, detail="Something gone wrong. Exception was raised."
        ) from e

    similar = "no"

    if is_match is True:
        similar = "yes"
    else:
        similar = "no"

    response["similar"] = similar
    return response
