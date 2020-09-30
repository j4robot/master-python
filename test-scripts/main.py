class Helper():

    def __init__(self) -> None:
        return None
    
    def fibonacci(self, num):
        '''This is a function for running a fibonacci sequence.
        
        It takes an int as the argument to show how many times the process is run. 
        '''
        a, b = 0, 1
        temp = []
        while a < num:
            temp.append(a)
            a, b = b, a + b
        return temp 

    def hand_total(self, hand):
        total = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                aces += 1
            else:
                total += int(card)
                
        total += aces
        while total + 10 <= 21 and aces > 0:
            total += 10
            aces -= 1
        return total

    def best_items(self, racers):
        """Given a list of racer dictionaries, return a dictionary mapping items to the number
        of times those items were picked up by racers who finished in first place.
        """
        winner_item_counts = {}
        for i in range(len(racers)):
            # The i'th racer dictionary
            racer = racers[i]
            # We're only interested in racers who finished in first
            if racer['finish'] == 1:
                for x in racer['items']:
                    # Add one to the count for this item (adding it to the dict if necessary)
                    if x not in winner_item_counts:
                        winner_item_counts[i] = 0
                    winner_item_counts[i] += 1

            # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
            if racer['name'] is None:
                print(f"WARNING: Encountered racer with unknown name on iteration {i + 1}/{len(racers)} (racer = {racer['name']})")
        return winner_item_counts