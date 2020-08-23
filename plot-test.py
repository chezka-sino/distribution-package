from distributions import Binomial

binomial_one = Binomial()
binomial_one.read_data_file('numbers_binomial.txt')
binomial_one.replace_stats_with_data()
binomial_one.plot_bar()
binomial_one.plot_bar_pdf()