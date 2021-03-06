#!/usr/bin/env python3
#
# Copyright 2020 Sage Sharp <sharp@otter.technology>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Create a set of generic form emails when we don't have a resume match.

import argparse
import csv

def print_percentage(name, partial, total):
    print('{}: {:.0f}% ({})'.format(name, float(partial / total * 100), partial))

def race_and_ethnicity_demographics(data):
    # demographics:
    # 'What is your race and ethnicity? (Select all that apply)/Asian'
    total_alums = 0
    asian_alums = 0
    black_alums = 0
    hispanic_or_latinx_alums = 0
    indigenous_alums = 0
    middle_eastern_alums = 0
    white_alums = 0
    disadvantaged_caste = 0
    disadvantaged_tribe = 0
    for index, row in enumerate(data):
        total_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/Asian'] == '1':
            asian_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/Black'] == '1':
            black_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/Hispanic or Latinx'] == '1':
            hispanic_or_latinx_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/Indigenous'] == '1':
            indigenous_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/Middle Eastern'] == '1':
            middle_eastern_alums += 1
        if row['What is your race and ethnicity? (Select all that apply)/White'] == '1':
            white_alums += 1
        if row['Are you a member of a historically disadvantaged caste / scheduled caste?'] == 'Yes':
            disadvantaged_caste += 1
        if row['Are you a member of a historically disadvantaged tribe?'] == 'Yes':
            disadvantaged_tribe += 1

    print('Total alums: {}'.format(total_alums))
    print_percentage('Asian', asian_alums, total_alums)
    print_percentage('Black', black_alums, total_alums)
    print_percentage('Hispanic or Latinx', hispanic_or_latinx_alums, total_alums)
    print_percentage('Middle Eastern', middle_eastern_alums, total_alums)
    print_percentage('White', white_alums, total_alums)
    print_percentage('Historically disadvantaged caste or scheduled caste', disadvantaged_caste, total_alums)
    print_percentage('Historically disadvantaged tribe', disadvantaged_tribe, total_alums)

def gender_identities_demographics(data):
    # demographics:
    # 'What is your gender identity? (Select all that apply)/Woman'
    total_alums = 0
    men_alums = 0
    women_alums = 0
    non_binary_alums = 0
    other_gender_identity = 0
    cis_alums = 0
    trans_alums = 0
    for index, row in enumerate(data):
        total_alums += 1
        if row['What is your gender identity? (Select all that apply)/Man'] == '1':
            men_alums += 1
        if row['What is your gender identity? (Select all that apply)/Woman'] == '1':
            women_alums += 1
        if row['What is your gender identity? (Select all that apply)/Non-binary'] == '1':
            non_binary_alums += 1
        if row["What is your gender identity? (Select all that apply)/My gender isn't listed here"] == '1':
            other_gender_identity += 1

        if row['Do you identify as transgender?'] == 'No':
            cis_alums += 1
        elif row['Do you identify as transgender?'] == 'Yes':
            trans_alums += 1

    print("")
    print("Gender Identities")
    print("---")
    print_percentage('Men', men_alums, total_alums)
    print_percentage('Women', women_alums, total_alums)
    print_percentage('Non-binary', non_binary_alums, total_alums)
    print_percentage('Other gender identity', other_gender_identity, total_alums)
    print_percentage('Cisgender', cis_alums, total_alums)
    print_percentage('Transgender', trans_alums, total_alums)

def before_outreachy_statistics(data):
    # overview:
    # 'In the three months before your Outreachy internship, were you:'
    #  - "A student"
    #  - "Employed"
    #  - "Unemployed"
    #  - "Other"
    #  - "A full-time parent"
    student_applicants = 0
    employed_applicants = 0
    unemployed_applicants = 0
    other_applicants = 0
    parent_applicants = 0
    total_applicants = 0

    print()
    print("Before Outreachy")
    print("---")
    print()

    for index, row in enumerate(data):
        total_applicants += 1
        if row['In the three months before your Outreachy internship, were you:'] == 'A student':
            student_applicants += 1
        elif row['In the three months before your Outreachy internship, were you:'] == 'Employed':
            employed_applicants += 1
        elif row['In the three months before your Outreachy internship, were you:'] == 'Unemployed':
            unemployed_applicants += 1
        elif row['In the three months before your Outreachy internship, were you:'] == 'A full time parent':
            parent_applicants += 1
        elif row['In the three months before your Outreachy internship, were you:'] == 'Other':
            other_applicants += 1
            print("Other:", row['In the three months before your Outreachy internship, what was your employment or educational situation?'])

    print()
    print('Total alums: {}'.format(total_applicants))
    print_percentage('Students', student_applicants, total_applicants)
    print_percentage('Employed', employed_applicants, total_applicants)
    print_percentage('Unemployed', unemployed_applicants, total_applicants)
    print_percentage('Parents', parent_applicants, total_applicants)
    print_percentage('Other', other_applicants, total_applicants)

def retention_statistics(data):
    # overview:
    # 'Are you currently:'
    #  - "A student"
    #  - "Employed"
    #  - "Unemployed"
    #  - "Other"
    #  - "A full-time parent"
    student_alums = 0
    stem_student_alums = 0
    student_alums_who_use_foss_in_school = 0
    student_alums_who_contribute_to_foss_in_school = 0
    employed_alums = 0
    tech_employed_alums = 0
    sponsor_employed_alums = 0
    employed_alums_who_use_foss_at_work = 0
    employed_alums_who_contribute_to_foss_at_work = 0
    unemployed_alums = 0
    other_alums = 0
    parent_alums = 0
    total_alums = 0

    print()
    print("Current Employment and Education status of alums")
    print("---")
    print()
    for index, row in enumerate(data):
        total_alums += 1
        if row['Are you currently:'] == 'A student':
            student_alums += 1
            if row['Are you a student in a science, technology, engineering, or mathematics field?'] == 'Yes':
                stem_student_alums += 1
            if row['Do you use free software / open source to complete your student projects or research?'] == 'Yes':
                student_alums_who_use_foss_in_school += 1
            if row['Do you contribute to free software / open source as part of your student projects or research?'] == 'Yes':
                student_alums_who_contribute_to_foss_in_school += 1
        elif row['Are you currently:'] == 'Employed':
            employed_alums += 1
            if row['Are you employed in the technology industry?'] == 'Yes':
                tech_employed_alums += 1
            if row['After your Outreachy internship, were you employed at any of the following Outreachy sponsors?/None of the above'] != '1':
                sponsor_employed_alums += 1
            if row['Does your job involve using free software / open source?'] == 'Yes':
                employed_alums_who_use_foss_at_work += 1
            if row['Does your job involve contributing to free software / open source?'] == 'Yes':
                employed_alums_who_contribute_to_foss_at_work += 1
        elif row['Are you currently:'] == 'Unemployed':
            unemployed_alums += 1
        elif row['Are you currently:'] == 'A full-time parent':
            parent_alums += 1
        elif row['Are you currently:'] == 'Other':
            other_alums += 1
            print("Other:", row['What is your current employment or educational situation?'])

    print()
    print('Total alums: {}'.format(total_alums))
    print_percentage('Students', student_alums, total_alums)
    print_percentage(' - STEM students', stem_student_alums, student_alums)
    print_percentage(' - Students who use FOSS for school projects or research', student_alums_who_use_foss_in_school, student_alums)
    print_percentage(' - Students who contribute to FOSS for school projects or research', student_alums_who_contribute_to_foss_in_school, student_alums)
    print_percentage('Employed', employed_alums, total_alums)
    print_percentage(' - Tech employees', tech_employed_alums, employed_alums)
    print_percentage(' - Employed by sponsor after internship', sponsor_employed_alums, employed_alums)
    print_percentage(' - Employees who use FOSS as part of their job', employed_alums_who_use_foss_at_work, employed_alums)
    print_percentage(' - Employees who contribute to FOSS as part of their job', employed_alums_who_contribute_to_foss_at_work, employed_alums)
    print_percentage('Unemployed', unemployed_alums, total_alums)
    print_percentage('Parents', parent_alums, total_alums)

def foss_retention(data):
    total_alums = 0
    use_foss = 0
    contribute_to_foss = 0
    do_not_contribute_to_foss = 0

    print()
    print("Retention in FOSS")
    print("---")
    print()
    for index, row in enumerate(data):
        total_alums += 1

        if row['In the last year, have you used free software / open source?'] == 'Yes':
            use_foss += 1

        if row['In the last year, have you contributed to free software / open source with:'] == 'No, I have not contributed to free software / open source in the last year':
            do_not_contribute_to_foss += 1
        elif row['In the last year, have you contributed to free software / open source with:'] != '':
            contribute_to_foss += 1

    print('Total alums: {}'.format(total_alums))
    print_percentage('Uses FOSS', use_foss, total_alums)
    print_percentage('Contributes to FOSS', contribute_to_foss, total_alums)
    print_percentage('Does not contribute to FOSS', do_not_contribute_to_foss, total_alums)

def gsoc_and_gsod_connections(data):
    total_alums = 0
    gsoc_intern = 0
    gsoc_mentor = 0
    gsoc_admin = 0
    gsod_intern = 0
    gsod_mentor = 0
    gsod_admin = 0

    print()
    print("Connection to GSoC and GSoD")
    print("---")
    print()
    for index, row in enumerate(data):
        total_alums += 1

        if row['After your Outreachy internship, did you participate in Google Summer of Code? (Select all that apply)/Yes, I was a GSoD intern'] == '1':
            gsoc_intern += 1
        if row['After your Outreachy internship, did you participate in Google Summer of Code? (Select all that apply)/Yes, I was a GSoD mentor'] == '1':
            gsoc_mentor += 1
        if row['After your Outreachy internship, did you participate in Google Summer of Code? (Select all that apply)/Yes, I was a GSoD org admin'] == '1':
            gsoc_admin += 1
        if row['After your Outreachy internship, did you participate in Google Season of Docs? (Select all that apply)/Yes, I was a GSoD intern'] == '1':
            gsod_intern += 1
        if row['After your Outreachy internship, did you participate in Google Season of Docs? (Select all that apply)/Yes, I was a GSoD mentor'] == '1':
            gsod_mentor += 1
        if row['After your Outreachy internship, did you participate in Google Season of Docs? (Select all that apply)/Yes, I was a GSoD org admin'] == '1':
            gsod_admin += 1

    print('Total alums: {}'.format(total_alums))
    print_percentage('Google Summer of Code intern after Outreachy', gsoc_intern, total_alums)
    print_percentage('Google Summer of Code mentor after Outreachy', gsoc_mentor, total_alums)
    print_percentage('Google Summer of Code org admin after Outreachy', gsoc_admin, total_alums)
    print_percentage('Google Season of Docs intern after Outreachy', gsod_intern, total_alums)
    print_percentage('Google Season of Docs mentor after Outreachy', gsod_mentor, total_alums)
    print_percentage('Google Season of Docs org admin after Outreachy', gsod_admin, total_alums)

def foss_talks(data):
    total_alums = 0
    gave_talk = 0

    print()
    print("Conference talks on FOSS")
    print("---")
    print()
    for index, row in enumerate(data):
        total_alums += 1

        if row['During or after your Outreachy internship, did you give a talk or presentation on free software/open source?'] == 'Yes':
            gave_talk += 1

    print('Total alums: {}'.format(total_alums))
    print_percentage('Gave a conference talks or presentation on FOSS', gave_talk, total_alums)

def mentorship(data):
    total_alums = 0
    outreachy_coordinator = 0
    outreachy_mentor = 0
    outreachy_volunteer = 0
    generic_mentor = 0

    print()
    print("Mentorship")
    print("---")
    print()
    for index, row in enumerate(data):
        total_alums += 1

        if row['After your Outreachy internship, did you volunteer for Outreachy? (Select all that apply)/Yes, I was an Outreachy coordinator'] == '1':
            outreachy_coordinator += 1
            print(row['First Name / Given Name'], row['Last Name / Family Name'], "Outreachy coordinator")
        if row['After your Outreachy internship, did you volunteer for Outreachy? (Select all that apply)/Yes, I was an Outreachy mentor'] == '1':
            outreachy_mentor += 1
            print(row['First Name / Given Name'], row['Last Name / Family Name'], "Outreachy mentor")
        if row['After your Outreachy internship, did you volunteer for Outreachy? (Select all that apply)/Yes, I was an informal Outreachy volunteer'] == '1':
            outreachy_volunteer += 1
        if row['After your Outreachy internship, did you become a mentor?'].startswith('Yes'):
            generic_mentor += 1

    print('Total alums: {}'.format(total_alums))
    print_percentage('Became Outreachy coordinator', outreachy_coordinator, total_alums)
    print_percentage('Became Outreachy mentor', outreachy_mentor, total_alums)
    print_percentage('Became Outreachy volunteer', outreachy_volunteer, total_alums)
    print_percentage('Became a mentor', generic_mentor, total_alums)

def print_successes(data):
    print()
    print("Success stories")
    print("---")
    print()
    for index, row in enumerate(data):
        if row['After your Outreachy internship, did you win any awards?'] != '':
            print("Award:", row['First Name / Given Name'], row['Last Name / Family Name'], row['After your Outreachy internship, did you win any awards?'])

        if row['After your Outreachy internship, did you take on any leadership roles?'] != '':
            print("Leadership role:", row['First Name / Given Name'], row['Last Name / Family Name'], row['After your Outreachy internship, did you take on any leadership roles?'])

        if row['Tell us more about your successes after Outreachy!'] != '':
            print("Success story:", row['First Name / Given Name'], row['Last Name / Family Name'], row['Tell us more about your successes after Outreachy!'])

        if row['After your Outreachy internship, did you win any awards?'] != '' or row['After your Outreachy internship, did you take on any leadership roles?'] != '' or row['Tell us more about your successes after Outreachy!'] != '':
            print()

def main():
    parser = argparse.ArgumentParser(description='Print statistics from 2019 Outreachy longitudinal survey')
    parser.add_argument('--csv', help='CSV file of longitudinal survey responses')
    parser.add_argument('--successes', help='Use `--successes 1` to print awards, leadership positions, and success stories of Outreachy alums')
    args = parser.parse_args()

    data = []
    with open(args.csv, 'r') as csvFile:
        freader = csv.DictReader(csvFile, delimiter=';', quotechar='"')
        for row in freader:
            data.append(row)

    race_and_ethnicity_demographics(data)
    gender_identities_demographics(data)
    before_outreachy_statistics(data)
    retention_statistics(data)
    foss_retention(data)
    gsoc_and_gsod_connections(data)
    foss_talks(data)
    mentorship(data)

    if args.successes == '1':
        print_successes(data)

if __name__ == "__main__":
    main()
