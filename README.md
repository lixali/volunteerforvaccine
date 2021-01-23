# volunteerforvaccine
Find an open shift to volunteer to distribute vaccine at a mass dispensing site in Los Angeles County

## Code

Crawler.py is the main script. openShift() is the primary function that loops through all the sites and all the weeks and looks for available shifts and if a day-shift slot doesn't say "All Shifts Filled" then it will send an SMS/Email to all the emails/SMS that people have provided. Everything is hard coded as of now but it shouldn't be. The links, the email address to send from, email address to send to, phone numbers to send SMS to. Need to create submission form to receive phone numbers and emails. Need to create config files. Make password secret/hidden from Github.

email_LFC.py is a module with a function to send email, called by crawler

SMS_LFC.py is a module with a function to send SMS, called by crawler

scheduler_no_available_slot.html - html of scheduler page when there aren't any available shifts

scheduler_available_slot.html - html of scheduler page when there aren't any available shifts

signup_form.html - html of signup form itself

## Scheduler Flow
Flow to sign up for a volunteer slot:
1) Home page for the scheduler system with information: https://appointments.lacounty.gov/vaccinestaffing
  -- Click "VOLUNTEER/STAFF SIGN UP" button to proceed to #2 (select site)

2) Shows each of the sites: https://appointments.lacounty.gov/vaccinestaffing/LocationsMap
  -- Pick a site, click "VIEW SHIFTS" then "NON-CLINICAL ROLE" to proceed to #3 (select date)

3) Shows next 7 days at specified site: https://appointments.lacounty.gov/vaccinestaffing/Calendar/63/3011
  -- The "63/3011/" part of directory defines the site location
  -- If you advance a page by clicking "NEXT WEEK MM/DD to MM/DD >" it advances by a week and adds page number to URL e.g. https://appointments.lacounty.gov/vaccinestaffing/Calendar/63/3011/1
  -- total of 4 pages of shifts = 4 weeks (last week ends on Sunday, may change)
  -- If you go back a page, page number is set to 0 (0 is default)
  -- Click "All Day Shift 8-6:30" to sign up for a shift on specified date at specified site, proceed to #4 (sign up form)

4) Form to officially sign up for a volunteer shift, enter personal identifying information etc 
  -- Click "SUBMIT" to submit form, confirmation is sent to email provided in form

## Site locations
Available sites:
Mega POD 1 – Pomona Fairplex
1101 W. Mckinley Ave Pomona, CA 91768

Mega POD 2 – The Forum
3900 W Manchester Blvd Inglewood, CA 90305

Mega POD 3 – CSU Northridge
18343 Plummer St Northridge, CA 91325

Mega POD 4 – LACOE – Ed Center West
12800 Ardis Ave Downey, CA 90242

Mega POD 5 – Six Flags Magic Mountain
26101 Magic Mountain Pkwy Valencia, CA 91355
