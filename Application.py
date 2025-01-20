import Course
from Old_Files import course_layout_HGC as HGC

if __name__ == '__main__':
    HendonGC = Course.GolfCourse(
        name="Hendon",
        description="Founded in 1903, Hendon Golf Club is the perfect venue for a round of golf, your special occasion,"
                    " business, or social event.",
        par=72,
        numholes=18
    )
    hole1 = HendonGC.add_hole(1, 4,'HGC/Hole1', 51.60409972788149, -0.21955174305143066)
    hole1.create_zone()
    hole1.print_map()
    hole1.save_to_csv()

    hole2 = HendonGC.add_hole(2, 4, 'HGC/Hole2', 51.601611471839774, -0.21897208954836292)
    hole2.create_zone()
    hole2.print_map()

    hole3 = HendonGC.add_hole(3, 4, 'HGC/Hole3', 51.59881966272524, -0.21591195114437856)
    hole3.create_zone()
    hole3.print_map()

    hole4 = HendonGC.add_hole(4,4, 'HGC/Hole4', 51.59991583429396, -0.2125143980881828)
    hole4.create_zone()
    hole4.print_map()

    hole5 = HendonGC.add_hole(5,4,'HGC/Hole5', 51.600330645834354, -0.2136038433931772)
    hole5.create_zone()
    hole5.print_map()

    print(HGC.hole1_bunker())
