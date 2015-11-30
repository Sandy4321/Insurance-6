from django.test import TestCase
from django.utils import timezone
from insurance.models import Branch, Underwriter, Customer

class InsuranceModelTest(TestCase):

	def test_creating_a_new_branch_and_saving_it_to_the_database(self):
        # start by creating a new Poll object with its "question" set
		branch = Branch()
		branch.name = "Ortigas branch"
		branch.address = "Ortigas Pasig, City"
        
        # check we can save it to the database
		branch.save()

        # now check we can find it in the database again
		all_branches_in_database = Branch.objects.all()
		self.assertEquals(len(all_branches_in_database), 1)
		only_branch_in_database = all_branches_in_database[0]
		self.assertEquals(only_branch_in_database, branch)

        # and check that it's saved its two attributes: question and pub_date
		self.assertEquals(only_branch_in_database.name, "Ortigas branch")
		self.assertEquals(only_branch_in_database.address, "Ortigas Pasig, City")

	def test_creating_a_new_underwriter_and_saving_it_to_the_database(self):
		
		underwriter = Underwriter()
		underwriter.name = "Pru Life UK"
		underwriter.address = "1554 Quezon Ave."
		underwriter.save()

		all_underwriters_in_database = Underwriter.objects.all()
		self.assertEquals(len(all_underwriters_in_database), 1)
		only_branch_in_database = all_underwriters_in_database[0]
		self.assertEquals(only_underwriter_in_database, underwriter)

        # and check that it's saved its two attributes: question and pub_date
		self.assertEquals(only_underwriter_in_database.name, "Pru Life UK")
		self.assertEquals(only_underwriter_in_database.address, "1554 Quezon Ave.")

#class HomePageViewTest(TestCase):

#	def test_root_url_shows_links_to_all_branches(self):
        # set up some polls
        #poll1 = Poll(question='6 times 7', pub_date=timezone.now())
        #poll1.save()
        #poll2 = Poll(question='life, the universe and everything', pub_date=timezone.now())
        #poll2.save()

		#response = self.client.get('/')

        # check we've used the right template
		#self.assertTemplateUsed(response, 'home.html')


    	# check we've passed the polls to the template
		#branches_in_context = response.context['branches']
		#self.assertEquals(list(polls_in_context), [poll1, poll2])
        # check the poll names appear on the page
        #self.assertIn(poll1.question, response.content)
        #self.assertIn(poll2.question, response.content)