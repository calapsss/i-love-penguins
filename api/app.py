from vetiver import *
import vetiver
import pins





model_name = 'penguin_model'
version = '20240309T005955Z-565d5'
dir = '/data/model/'
b = pins.board_folder(dir, allow_pickle_read=True)

v = VetiverModel.from_pin(b, model_name, version)
print(v)
vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
