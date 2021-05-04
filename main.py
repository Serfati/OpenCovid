from lib.config import *
from lib.plots import display_analyze
from lib.opencovid import OpenCoVid
from distance.social_distance import SocialDistance

sys.path.insert(0, 'yolomask/')
from yolomask.mask_inference import YoloMask
from yolomask.person_inference import YoloPerson


if __name__ == '__main__':
    # === OpenCoVid Lib Use =========================
    ocv = OpenCoVid(callback=display_analyze, video_src=video_src)

    # filters
    ocv.add_analyze_filter(YoloPerson())
    ocv.add_analyze_filter(SocialDistance())
    ocv.add_analyze_filter(YoloMask())

    # run
    ocv.analyze()
    # ===============================================
