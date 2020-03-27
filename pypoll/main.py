with open('election_data.csv') as election_data_file:
    # No votes counted yet
    votes_counted = 0

    # Start at line zero in computer land
    line_number = 0

    # The candiate list
    # Sets inately list of unique values
    # all_people = set()
    # create a dictionary and name it all ppl
    all_people = dict()

    # Loopy Loop
    # for each line in that file to the right
    for line in election_data_file:
        # if line number is greater than 0
        if line_number > 0:
            # create splits where commas are
            columns = line.split(',')
            # transform characters into numbers for column 0 and assign them voter_id as name
            # voter_id = int(columns[0])
            columns[0] = int(columns[0])
            # give column 1 name county
            # county = columns[1]
            # name column 2 candidate
            # candidate = columns[2].strip()
            columns[2] = columns[2].strip()
            # start at line 1, take next line and add to previous line
            votes_counted = votes_counted + 1

            # Bullet point 2
            # all_people.add(columns[2])
            # If you run into a name and its not in there, put it in
            if columns[2] not in all_people:
                all_people[columns[2]] = 0

            # Out of this dictionary, look at individuals in column 2
            # Now, take each name in column 2 and add 1 for each time it shows up
            all_people[columns[2]] = all_people[columns[2]] + 1

        line_number += 1

    with open('results.txt', 'w') as results_file:
        print('Election Results')
        print('Election Results', file=results_file)
        print('---------------------')
        print('---------------------', file=results_file)
        # Total votes: is the name. {votes_counted} is the thing we named above
        print(f'Total Votes: {votes_counted}')
        print(f'Total Votes: {votes_counted}', file=results_file)
        print('---------------------')
        print('---------------------', file=results_file)
        print(f'All Candidates: {all_people.keys()}')
        # Now we have the candidates and the number of votes for each candidate
        print('---------------------')
        print('---------------------', file=results_file)
        # The name of the candiate with the most votes
        max_candate_name = ''
        # The number of votes that the max candiate has
        max_candiate_votes = 0
        # Loop through all pairs of information, which are candidates and their respective votes
        for candidate_name, votes_for_candidate in all_people.items():
            # If the votes for the candiate we are looking at in this iteration of the loop is greater
            # than what we have recorded so far, replace the max candiate information with this candidate's
            # info.
            if votes_for_candidate > max_candiate_votes:
                max_candate_name = candidate_name
                max_candiate_votes = votes_for_candidate
            # Calculate the percentage of votes that were for this candidate.
            percentage = round(votes_for_candidate / votes_counted * 100, 3)
            print(f'{candidate_name}: {percentage}% ({votes_for_candidate})')
            print(f'{candidate_name}: {percentage}% ({votes_for_candidate})', file=results_file)
        print('---------------------')
        print('---------------------', file=results_file)
        print(f'Winner: {max_candate_name}')
        print(f'Winner: {max_candate_name}', file=results_file)
        print('---------------------', file=results_file)
