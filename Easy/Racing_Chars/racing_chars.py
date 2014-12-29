__author__ = "Sean R. Vinas"
__date__ = "3 December 2014"
__doc__ = """In this challenge you will be given a file where each line is a section of a race track with obstructions, gates and checkpoints. The goal is to find a way of passing this track, using the following rules:
Each section contains only a single gate or a gate with a checkpoint.
The race car can ride only through gates or checkpoints.
You should prefer driving through checkpoint rather then a gate.
The obstructions are represented by # (hash).
The gates are represented by _ (underscore).
The checkpoints are represented by C."""


from sys import argv


def prev_car_location(last_track):
    """ Returns an index of the last location the car was
    Args:
	last_track: A string representing a track
    Returns:
	An int of the last car location as an index
    For example:
    >>> prev_car_location('|##')
    0

    >>> prev_car_location('#\#')
    1

    >>> prev_car_location('##/')
    2

    >>> prev_car_location('##_')
    2
    """
    prev_car_turn_signals = '|/\\'
    for n, item in enumerate(last_track):
	if item in prev_car_turn_signals:
	    return n
    return last_track.index('_')


def start_track(track):
    """The start of a race track, choose the beginning path. Always |.
    Args:
	track: A string with a track
    Returns:
	A string with the chosen route
    For example:
    >>> start_track('##_##')
    '##|##'
    """
    loc = prev_car_location(track)
    return go_straight(track, loc, len(track))


def go_straight(next, loc, max_index):
    """
    Args:
	next: A string of the track
	loc: chosen index location for turn signal
	max_index: The index dictating the end of the track
    Returns:
	A track displaying the chosen path
    For example:
    >>> go_straight('#C#', 1, 2)
    '#|#'

    >>> go_straight('C##', 0, 2)
    '|##'
    """
	if loc + 1 <= max_index:
		return next[:loc] + '|' + next[loc+1:]
	return next[:loc] + '|'


def go_left(next, below):
    """
    Args:
	next: A string of the track
	below: chosen index location for turn signal
    Returns:
	A track displaying the chosen path
    For example:
	go_left('#C#', 1)
	'#/#'

	go_left('#C_', 1)
	'#/_'

	go_left('C_#', 1)
	'/_#'
    """
    return next[:below] + '/' + next[below+1:]


def go_right(next, above, max_index):
    """
    Args:
	next: A string of the track
	above: chosen index location for turn signal
	max_index: The index dictating the end of the track
    Returns:
    For example:
    #>>> go_right('#C#', 1, 3)
    '#\#'
    """
    if above + 1 <= max_index:
	return next[:above] + '\\' + next[above+1:]
    return next[:above] + '\\'


def look_ahead(current, next):
    """Determine the index of choice for the current.
    Args:
    Returns:
    For example:
    >>> look_ahead('##|##', '_C###')
    '_/###'

    >>> look_ahead('###|#', '##C_#')
    '##/_#'

    >>> look_ahead('####/#######', '###_#C######')
    '###_#\######'
    """
    straight = prev_car_location(current)
    right = straight+1
    left = straight-1
    max_index = len(next)-1
    for i in 'C_':
    	if next[straight] == i:
    	    return go_straight(next, straight, max_index)
	elif right <= max_index and next[right] == i:
	    return go_right(next, right, max_index)
	elif left >= 0 and next[left] == i:
	    return go_left(next, left)


def read_complete_track():
    """Read every line from text file
    Returns:
    	A list with each index containing a string track representation
    """
    tracks = []
    textfile = open(argv[1], 'r')
    for line in textfile:
    	tracks.append(line.rstrip('\n'))
    textfile.close()
    return tracks


def display_routes(tracks):
    """ Print out each track result."""
    result = ''
    track = 1
    result = start_track(tracks[0])
    print(result)
    while track < len(tracks):
    	result = look_ahead(result, tracks[track])
    	print(result)
    	track += 1


def main():
    """Read a text file and display results."""
    tracks = read_complete_track()
    display_routes(tracks)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
