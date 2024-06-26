import csv
import os


# Variables
vote_counts=0
candidate_names =[]
candidate_votes ={}
winner = [0,""]
# File Path
input_path=os.path.join("Resources", "election_data.csv")
output_path=os.path.join("analysis", "election_results.txt")


# With Open Stmt
with open(input_path) as data:
    reader = csv.reader(data)
    header = next(reader)

    #For Loop 
    for row in reader:
        vote_counts+=1
        name = row[2]

        # Conditon - Check if Candidate Name in  List
        if name not in candidate_names:
            candidate_names.append(name)
            candidate_votes[name]=0

        # Count Votes
        candidate_votes[name]+=1

# With Open Stmt to Write
with open(output_path, "w")as file:
    election_results=(
        f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {vote_counts}\n"
        f"----------------\n"
    )

    print(election_results)

    file.write(election_results)


    for candidate in candidate_votes:
        vote=candidate_votes.get(candidate)
        percentage=float(vote)/vote_counts*100
        if vote > winner[0]:
            winner[0]=vote
            winner[1]=candidate

        candidate_results=f"{candidate}: {percentage: .3f}% ({vote})\n"
        print(candidate_results)

        file.write(candidate_results)

    winner_result =(
       f"----------------\n"
        f"Winner: {winner[1]}\n"
        f"----------------\n" 
    )

    print(winner_result)

    file.write(winner_result)
