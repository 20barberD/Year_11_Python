aVotes = 0
bVotes = 0
cVotes = 0

needsToEnd = False
while not needsToEnd:
    vote = input("Type A, B, or C to vote for someone: ").lower()
    match(vote):
        case "a":
            aVotes += 1
            print("Voted for Candidate A ")
        case "b":
            bVotes += 1
            print("Voted for Candidate B ")
        case "c":
            cVotes += 1
            print("Voted for Candidate C ")
        case "end":
            needsToEnd = True
            print("VOTING ENDED ")
        case other:
            print("That's not a candidate! ")

print(f"Votes for Candidate A: {aVotes}\nVotes for Candidate B: {bVotes}\nVotes for Candidate C: {cVotes}\nTotal votes: {aVotes+bVotes+cVotes}")