import fresh_tomatoes
import media


#favourite movies details.
first_collections = media.favourite_movies("Born Free", 
					"https://thumbs.dreamstime.com/z/portrait-cute-small-boy-playing-meadow-kid-32065995.jpg",
					"https://www.youtube.com/watch?v=kr3b52OFucY")

second_collections = media.favourite_movies("Half Ticket",
					"https://computing.ece.vt.edu/~santol/projects/zsl_via_visual_abstraction/interact/interact_illustration_instance_dataset/imgs/20YSVQ8H88MQHFYB76MCO1R2GRY7QY_11.jpg",
					"https://www.youtube.com/watch?v=nJfkan5GqL8")

third_collections = media.favourite_movies("Arranged Marriage", 
					"https://tse4.mm.bing.net/th?id=OIP.KS_61Y54eHsb0Xx2tdwLvwEsEs&pid=15.1&P=0&w=300&h=300", 
					"https://www.youtube.com/watch?v=fOzFn-L2XO0")

fourth_collections = media.favourite_movies("invasion", 
					"http://www.indianfunpic.com/wp-content/uploads/2016/08/Funny-114.jpg", 
					"https://www.youtube.com/watch?v=oy_ZRLzIOGc")

fifth_collections = media.favourite_movies("positive", 
					"http://www.zwani.com/graphics/hello_funny/images/56467.jpg", 
					"https://www.youtube.com/watch?v=evsjTDgPeAU")

sixth_collections = media.favourite_movies("Afterglow", 
					"https://s-media-cache-ak0.pinimg.com/736x/19/0f/95/190f95dd8a0cc53851d1ce3358e10282--funny-jokes-funny-sayings.jpg", 
					"https://www.youtube.com/watch?v=_f2ErhTh7QM")

seventh_collections = media.favourite_movies("Unarranged", 
					"https://c1.staticflickr.com/5/4186/33750814364_d136da9a4c_b.jpg", 
					"https://www.youtube.com/watch?v=RnRmgAFpv3s")


# list of favourite movies which is passed to the open_movies_page function
collections = [first_collections, second_collections, third_collections, fourth_collections, fifth_collections, seventh_collections]
fresh_tomatoes.open_movies_page(collections)
