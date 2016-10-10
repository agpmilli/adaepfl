# 02 - Data from the Web

## Deadline
Monday October 17, 2016 at 11:59PM

## Important Notes
* Make sure you push on GitHub your Notebook with all the cells already evaluated (i.e., you don't want your colleagues to generate 
unnecessary Web traffic during the peer review :)
* Don't forget to add a textual description of your thought process, the assumptions you made, and the solution
you plan to implement!
* Please write all your comments in English, and use meaningful variable names in your code

## Background
In this homework we will extract interesting information from [IS-Academia](http://is-academia.epfl.ch/page-6228.html), the educational
portal of EPFL. Specifically, we will focus on the part that allows [public access to academic data](http://is-academia.epfl.ch/publicaccess-Bachelor-Master).
The list of registered students by section and semester is not offered as a downloadable dataset, so you will have to find a way to scrape the
information we need. On [this form](http://isa.epfl.ch/imoniteur_ISAP/%21gedpublicreports.htm?ww_i_reportmodel=133685247) you can select
the data to download based on different criteria (e.g., year, semester, etc.)

You are not allowed to download manually all the tables -- rather you have to understand what parameters the server accepts, and
generate accordingly the HTTP requests. For this task, [Postman](https://www.getpostman.com) with the [Interceptor extension](https://www.getpostman.com/docs/capture)
can help you greatly. I recommend you to watch this [brief tutorial](https://www.youtube.com/watch?v=jBjXVrS8nXs&list=PLM-7VG-sgbtD8qBnGeQM5nvlpqB_ktaLZ&autoplay=1)
to understand quickly how to use it.
Your code in the iPython Notebook should not contain any hardcoded URL. To fetch the content from the IS-Academia server,
you can use the [Requests](http://docs.python-requests.org/en/master/) library with a Base URL, but all the other form parameters
should be extracted from the HTML with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
You can choose to download Excel or HTML files -- they both have pros and cons, as you will find out after a quick check. You can also
choose to download data at different granularities (e.g., per semester, per year, etc.) but I recommend you not to download all the data
in one shot because 1) the requests are likely to timeout and 2) we will overload the IS-Academia server.

## Assignment
We will focus exclusively on the academic unit `Informatique`. When asked, select the right [statistical test](http://hamelg.blogspot.ch/2015/11/python-for-data-analysis-part-24.html).

1. Obtain all the data for the Bachelor students, starting from 2007. Keep only the students for which you have an entry for both `Bachelor
semestre 1` and `Bachelor semestre 6`. Compute how many months it took each student to go from the first to the sixth semester. Partition
the data between male and female students, and compute the average -- is the difference in average statistically significant?

2. Perform a similar operation to what described above, this time for Master students. Notice that this data is more tricky, as there are
many missing records in the IS-Academia database. Therefore, try to guess how much time a master student spent at EPFL by at least checking
the distance in months between `Master semestre 1` and `Master semestre 2`. If the `Mineur` field is *not* empty, the student should also
appear registered in `Master semestre 3`. Last but not the least, don't forget to check if the student has an entry also in the `Projet Master`
tables. Once you can handle well this data, compute the "average stay at EPFL" for master students. Now extract all the students with a 
`Spécialisation` and compute the "average stay" per each category of that attribute -- compared to the general average, can you find any
specialization for which the difference in average is statistically significant?

3. *BONUS*: perform the gender-based study also on the Master students, as explained in 1. Use scatterplots to visually identify changes
over time. Plot males and females with different colors -- can you spot different trends that match the results of your statistical tests?
