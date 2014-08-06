import random

def main():
    states = {'Alabama': 9, 'Alaska': 3, 'Arizona': 11, 'Arkansas': 6,
              'California': 55, 'Colorado': 9, 'Connecticut': 7,
              'Delaware': 3, 'District of Columbia': 3, 'Florida': 29,
              'Georgia': 16, 'Hawaii': 4, 'Idaho': 4, 'Illinois': 20,
              'Indiana': 11, 'Iowa': 6, 'Kansas': 6, 'Kentucky': 8,
              'Louisiana': 8, 'Maine': 4, 'Maryland': 10, 'Massachusetts': 11,
              'Michigan': 16, 'Minnesota': 10, 'Mississippi': 6,
              'Missouri': 10, 'Montana': 3, 'Nebraska': 5, 'Nevada': 6,
              'New Hampshire': 4, 'New Jersey': 14, 'New Mexico': 5,
              'New York': 29, 'North Carolina': 15, 'North Dakota': 3,
              'Ohio': 18, 'Oklahoma': 7, 'Oregon': 7, 'Pennsylvania': 20,
              'Rhode Island': 4, 'South Carolina': 9, 'South Dakota': 3,
              'Tennessee': 11, 'Texas': 38, 'Utah': 6, 'Vermont': 3,
              'Virginia': 13, 'Washington': 12, 'West Virginia': 5,
              'Wisconsin': 10, 'Wyoming': 3}

    issues = ['Campaign Finance', 'Censorship and the Internet',
              'Child Support', 'Church State', 'Civil Rights',
              'Climate Change / Global Warming', 'Crime', 'Death Penalty',
              "Don't-Ask-Don't-Tell", 'Drug Policy', 'Education',
              'Energy independence', 'Energy & Oil', 'Environment', 'Firearms',
              'Flat Tax', 'Foreign Policy', 'Free Trade', 'Gay Rights',
              'Gun Control', 'Health Care', 'Homeland Security',
              'Illegal Immigrants', 'Immigration','Increase military spending',
              'Infrastructure & Technology', 'Internet Censorship', 'Language',
              'Medical Marijuana', 'Medicare & Medicaid', 'NAFTA',
              'Nuclear Energy & Weapons', 'Nuclear Testing', 'Patient Rights',
              'Political Corruption', 'Privacy on the Internet',
              'Political Issues', 'Race Relations', 'School Prayer',
              'Social Security', 'State of the Union', 'Stem Cells',
              'Tax Reform', 'Terrorism', 'Tobacco', 'Unemployment',
              'Universal Health Care', 'Veterans', 'Voting Rights',
              'War & Peace', 'War on Terror', 'Wealth Inequality',
              'Weapons of Mass Destruction', 'Welfare and Poverty']

    x = random.sample([4, 6, 8, 12, 16, 18, 24, 32, 42, 48, 50,len(issues)], 4)
    for i in x:
        file_name = './' + str(i) + '_issues.txt'
        outfile = open(file_name,"w")
        outfile.write('Social issues: ')
        outfile.write(str(i))
        outfile.write('\n')
        outfile.write('\n')
        for issue in issues[:i]:
            outfile.write(issue)
            outfile.write(': ')
            outfile.write(str(random.randint(50000, 2000000)))
            outfile.write('\n')
        outfile.write('\n')
        for state, vote in states.iteritems():
            outfile.write(state)
            outfile.write('\n')
            outfile.write('Votes: ')
            outfile.write(str(vote))
            outfile.write('\n')
            for issue in issues[:i]:
                outfile.write(issue)
                outfile.write(': ')
                outfile.write(str(random.randint(0, 20)))
                outfile.write('\n')
            outfile.write('\n')
        outfile.close()

if __name__ == '__main__':
    main()
