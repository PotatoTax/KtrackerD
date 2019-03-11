import main
import SheetTools


class ActivityData:

    def __init__(self, data):
        # Parses data from array into object
        self.sport = data[0]
        self.title = data[1]
        self.time = data[2]
        self.distance = data[3]
        self.description = data[4]
        self.id = data[5]

        # Array off all information
        self.attributes = [
            self.sport,
            self.title,
            self.time,
            self.distance,
            self.description,
            self.id
        ]

    def add(self):
        # Parses data back into array
        data = [0 for _ in range(6)]
        for a in range(len(self.attributes)):
            data[a] = self.attributes[a]

        # Adds the activity to the database
        SheetTools.add_activity(
            main.currentUser,
            data
        )

    def edit(self, old_activity):
        # Parses new and old data for activity
        new = [0 for _ in range(6)]
        old = [0 for _ in range(6)]
        for a in range(len(self.attributes)):
            new[a] = self.attributes[a]
            old[a] = old_activity.attributes[a]

        # Saves all necessary edits to database
        SheetTools.edit_activity(
            main.currentUser,
            new,
            old
        )
