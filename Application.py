import Course
from Hole import *
from Course import *
import course_layout_HGC as HGC

if __name__ == '__main__':
    HendonGC = Course.GolfCourse(
        name="Hendon",
        description="Founded in 1903, Hendon Golf Club is the perfect venue for a round of golf, your special occasion,"
                    " business, or social event.",
        par=72,
        numholes=18
    )
    hole1 = HendonGC.add_hole(1, 4)
    hole1.add_zone(
        coordinates=HGC.hole1_zone()
    )
    hole1.add_fairway(
        coordinates=HGC.hole1_fairway()
    )
    hole1.add_green(
        coordinates=HGC.hole1_green()
    )
    hole1.add_bunker(
        coordinates=HGC.hole1_bunker()
    )
    hole1.add_treeline(
        coordinates=HGC.hole1_treeline()
    )
    hole1.add_teebox(
        coordinates=HGC.hole1_teebox()
    )
    hole1.add_centre(51.60409972788149, -0.21955174305143066)

    hole1.print_map()

    print(HGC.hole1_bunker())
