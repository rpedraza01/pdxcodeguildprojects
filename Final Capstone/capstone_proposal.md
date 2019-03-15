#**Capstone Proposal**

**App Name:** Muqrakr (muqrakr.com)

##**Project Overview:**
The problems Muqrakr is trying to solve are the following:
-Give people a one-stop-shop for finding information on political candidates, sitting Congressional members, campaign committees, and lobbyists who contribute to campaign committees - greater accessibility and usability.
-Allow users to contact their elected officials from within the site - no need to leave or be redirected to another site to contact the elected officials.
-Allow users to quickly filter, gather, and download data to use in their own data visualizations and analyses.
-Better inform people how politics is funded and who is funding it and how that influences the decisions of elected officials.

##**APIs, Libraries, and Frameworks:**
Muqrakr will use the ProPublica Campaign Finance API. It will use the Skeleton CSS framework for styling. It will also use the Vue.js framework for building the user interfaces. It will also use Beautiful Soup parsing library for screen scraping the contact information users want in order to create a simple auto-generated form to fire off an email to a member of Congress.

##**User Stories:**
-“As a voter I want to be able to see who is contributing to a candidate’s political campaign and with that information decide who I should support or oppose.”
	-Tasks:
		-Make candidate information and finances easily searchable and filterable.
		-Display candidate information and finances.
-“As someone who closely follows politics, I want to be able to save my searches, and download selected data to a CSV file for my own statistical analysis.”
	-Tasks:
		-Save user searches for faster future querying.
		-Allow users to download selected data.
		-Allow users to select multiple candidates and/or committees for comparison.
		-Allow users to create a profile.
-“As someone who is mad as hell at elected officials X, Y, and Z, I want a one-stop-shop to look up selected information and fire off some angry emails.”
	-Tasks:
		-Scrape candidate/committee sites for contact info and create a form that allows users to send off an email from a form generated on my site.

##**Features:**
-Lookup information on political candidates
	-Candidate info-
		-FEC Candidate ID number
		-Candidate name
		-Party affiliation
		-State and/or House district
		-Date of Birth
		-Gender
		-.house.gov or .senate.gov url and social -media presence
		-Bills sponsored and/or cosponsored
		-Missed votes %
		-Votes with their party %
		-Committee assignments

	-Campaign committee info-
		-FEC Campaign Committee ID number
		-Committee name
		-Treasurer
		-Party affiliation
		-Street address
		-Financial info:
			-Total receipts
			-Total contributions from individuals
			-Total contributions from PACs
			-Total contributions
			-Total disbursements
			-Beginning cash
			-Ending cash
			-Total refunds
			-Debts owed
			-Total independent expenditures
	-Lobbyist bundlers for the campaign committee
		-FEC filing ID number
		-Transaction ID number
		-Lobbyist name
		-Lobbyist street address
		-Lobbyist employer
		-Lobbyist occupation
		-Amount collected and contributed
		-Date collected and contributed

-Filter capabilities
	-By state
	-Gender
	-Party affiliation
	-Congressional committees
	-Election year
	-Top 20 candidates in x-category (e.g. top 20 recipients of PAC donations)
-Auto-generated contact form for a specified candidate
	-Scrape contact info from congressional websites and social media sites
	-Click a button that brings up a form with a the candidates email filled-in and has a title field and text field for the message
	-Can also get candidate’s office phone number(s) so user can call
-User can select different information they would like to download to a CSV file for their own use (e.g. data visualization and statistical analysis)
-Users can create a profile to save their searches for future reference and faster querying

##**Data Model:**
Muqrakr will need to store the following information:
-User profiles
	-Login info
-Searches made by users for future use and faster querying
-It will need to save the different data that a user wants to get about a candidate, committee, lobbyist etc. for downloading to a CSV file.

##**Schedule:**
-**3/8/19 - 3/10/19 -** Begin and (hopefully) complete the Vue.js and Django tutorials.
-**3/11/19 -** Have capstone proposal completed and submitted. Begin Django and HTML/CSS work.
-**3/14/19 -** Have wireframing and Trello board completed.
-**3/17/19 -**  Have the Candidate and Campaign Committee search feature at a working state (use Javascript)
-**3/20/19 -** Have the filtering feature at a working state (at least to filter by state and election year) (use Javascript and/or Vue.js)
-**3/23/19 -** Have the auto-generated contact form at a working state (will require Beautiful Soup to scrape the necessary contact info ??).
-**3/26/19 -** Complete the feature that lets users select multiple candidates/committees/lobbyists and download that data to a CSV (use Python).
-**3/29/19 -** Users can create a profile to save their searches (use Django).
-**3/29/19 - 3/31/19 -** Extra time incase the need arises to fix something or not able to meet one of the aforementioned deadlines. Also, use time to put finishing touches on HTML/CSS and Django.
-**4/1/19 -** Final Capstone presentation.

##**What constitutes an MVP?:**
-Priority one “essential” features - 
	-Candidate/committee/lobbyist search and filtering.
-Priority two “Really-great-to-have” features - 
	-Auto-generated contact form.
-Priority three “Nice-to-have” features - 
	-Users can create a profile and save their searches. 
	-Users can select multiple candidates/committees/lobbyists and download that data to a CSV.
-Priority four “Really really-nice-to-have” features - 
	-Add in more searchable info about sitting members of Congress using the ProPublica Congress API. 
	-Also, adding some narrative about the current state of campaign finance (what is a PAC/Super PAC?, contribution limits, why political campaigns cost so much, what’s Citizen’s United)
