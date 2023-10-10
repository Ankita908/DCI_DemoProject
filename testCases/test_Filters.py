from pageObjects.homePage import SelectFilters


class TestFilters:


        def test_homepage_title(self,setup):
                self.driver = setup
                page_title = self.driver.title
                self.driver.close()
                if page_title == "Digital CI":
                        assert True
                else:
                        assert False

        def test_select_frequency(self,setup):
                self.driver = setup
                # timerange = SelectFilters(self.driver)
                # timerange.select_timerange()
                frequency = SelectFilters(self.driver)
                frequency.select_frequency()
                if frequency.frequency_option.text in frequency.time_interval_bubble:

                        assert True
                        self.driver.close()
                else:
                        self.driver.save_screenshot(".\\screenShots\\" + "test_select_frequency.png")
                        self.driver.close()
                        assert False
                #assert self.sf.selected_option.text in self.sf.time_interval_bubble.text

        def test_select_calculationcontext(self,setup):
                self.driver = setup
                calculation_context = SelectFilters(self.driver)
                calculation_context.select_calculationcontext()
                if calculation_context.calculation_option.text in calculation_context.calculation_bubble:

                        assert True
                        self.driver.close()
                else:
                        self.driver.save_screenshot(".\\screenShots\\" + "test_select_calculationcontext.png")
                        self.driver.close()
                        assert False

        def test_select_displaycontent(self, setup):
                self.driver = setup
                display_content = SelectFilters(self.driver)
                display_content.select_displaycontent()
                if display_content.displaycontent_option in display_content.displaycontent_bubble:
                        assert True
                else:
                        assert False

        #         self.assertIn(display_content.displaycontent_option, display_content.displaycontent_bubble)
        #
        # def assertIn(self, displaycontent_option, displaycontent_bubble):
        #         pass



