import sys
from pyvttl.vttl_api import VttlApi
from pyvttl.vttl_types import ShowDivisionNameType
from pyvttl.province import Province

# Example usage of the VttlApi wrapper

def main():
    # You can provide username/password if you want to test authenticated endpoints
    username = None  # Replace with your username if needed
    password = None  # Replace with your password if needed
    api = VttlApi(username=username, password=password)

    print("\nAvailable seasons:")
    print(api.getSeasons())

    # Get clubs and all possible values for Category and CategoryName
    print("\nClubs:")
    print(api.getClubs())
    print("\nUnique Category/CategoryName combinations:")
    unique_categories = Province.getVTTLProvinceDefinition(api_instance=api)
    for cat, cat_name in sorted(unique_categories):
        print(f"ProvinceID: {cat}, ProvinceName: {cat_name}")

    # Get clubs in province
    print("\nClubs in Province Vlaams-Brabant:")
    print(api.getClubs(province=Province.VLAAMS_BRABANT))

    # Get a specific club
    print("\nClub:")
    print(api.getClubs(club='Vl-B234'))

    print("\nTeams for club 'Vl-B234' in current season:")
    print(api.getClubTeams(club='Vl-B234'))

    print("\nDivisions:")
    print(api.getDivisions(show_division_name=ShowDivisionNameType.YES)) 


    print("\nMatches for club 'Vl-B234':")

    matches = api.getMatches(club='Vl-B234')
    # Sort matches by Date and Time
    def match_sort_key(match):
        return (str(match.Date), str(match.Time))

    sorted_matches = sorted(matches.TeamMatchesEntries, key=match_sort_key)

    # Print table header
    print(f"{'Week':<6} {'Date':<12} {'Time':<6} {'HomeClub':<10} {'HomeTeam':<20} {'AwayClub':<10} {'AwayTeam':<20} {'DivisionId':<10}")
    print('-' * 100)

    for match in sorted_matches:
        week = match.WeekName
        date = match.Date
        time = match.Time
        home_club = match.HomeClub
        home_team = match.HomeTeam
        away_club = match.AwayClub
        away_team = match.AwayTeam
        division_id = match.DivisionId
        date = date.strftime('%Y-%m-%d') if date is not None else ""
        time = time.strftime('%H:%M') if time is not None else ""
        print(f"{week:<6} {date:<12} {time:<6} {home_club:<10} {home_team:<20}  {away_club:<10} {away_team:<20}  {division_id:<10}")


    print("\nDivision ranking for division '8760':")
    print(api.getDivisionRanking(divisionId='8760'))


    print("\nMatch systems:")
    print(api.getMatchSystems())


    print("\nMembers of club 'Vl-B234':")
    members = api.getMembers(club='Vl-B234')
    # Output FirstName, LastName, Ranking for each member
    entries = members.MemberEntries if hasattr(members, 'MemberEntries') else []
    for member in entries:
        first = member.FirstName 
        last = member.LastName 
        ranking = member.Ranking 
        print(f"{first+' '+last:<30} - {ranking}")


    print("\nPlayer categories:")
    print(api.getPlayerCategories())

    print("\nTournaments:")
    print(api.getTournaments()) 

if __name__ == "__main__":
    main()
