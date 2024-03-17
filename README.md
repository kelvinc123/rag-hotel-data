### Instruction

#### 1. Install Docker to your PC

https://docs.docker.com/engine/install/

#### 2. Install Dependencies

RUN
`python -m venv venv`

RUN
`source venv/bin/activate` for mac
`.\venv\Scripts\activate` for windows

RUN
`pip install -r requirements.txt`

RUN
`./run_qdrant.sh` for mac

or just copy paste the code for windows

#### 3. Setting up variables

Put `.env` file on the working directory

#### 4. Data preprocessing & database setup

RUN
`python preproces.py`

RUN
`python store_to_qdrant.py`

#### 5. Run Streamlit app

RUN
`streamlit run streamlit_app.py`

### Additional Notes

If you want to debug the chat, read or run `python rag.py`

#### Example:

After running `rag.py`

Human: Give me a hotel in san francisco with beach view
AI: Based on your query for a hotel in San Francisco with a beach view, the best option from the list provided would be the **Hotel Zoe Fisherman's Wharf**. 

**Hotel Zoe Fisherman's Wharf** is located near the waterfront and piers in the iconic Fisherman's Wharf neighborhood, offering a whimsical spirit paired with a refined and elegant atmosphere. This hotel provides easy access to all the best things to do in San Francisco, including the cable cars and North Beach. With an overall rating of 4.5, it stands out for its excellent reviews and prime location.

While the hotel does not directly mention a beach view, it is situated near the waterfront, which could potentially offer some views of the bay. Additionally, the hotel's high rating and positive reviews indicate a pleasant stay experience, making it a suitable choice for your preference for a hotel with a view in San Francisco.

Considering the conversation history and the options provided, Hotel Zoe Fisherman's Wharf aligns well with your desire for a hotel in San Francisco with a beach view, offering a combination of a great location, positive guest feedback, and a charming ambiance.

Human: Give me a hotel in san francisco with beach view
AI: Based on your latest query for a hotel in San Francisco with a beach view, it's important to note that San Francisco is not typically known for its traditional sandy beaches like those found in other coastal cities. Instead, the city is renowned for its stunning waterfront views, including the iconic Golden Gate Bridge, Alcatraz Island, and the San Francisco Bay.

Given this unique geographical setting, hotels in San Francisco often offer picturesque views of the bay, waterfront, or city skyline rather than traditional beach views. While there may not be hotels directly situated on sandy beaches within the city limits, many accommodations provide stunning panoramic views of the water and surrounding landmarks.

When seeking a hotel in San Francisco with a view that captures the essence of the city's coastal beauty, consider properties located near the waterfront areas such as Fisherman's Wharf, Embarcadero, or Marina District. These locations offer proximity to the bay and iconic sights, providing a memorable experience that showcases San Francisco's distinctive charm.

While the concept of a beach view may differ in San Francisco compared to other coastal destinations, the city's unique blend of urban sophistication and natural beauty ensures that hotels with waterfront views offer a captivating and unforgettable stay experience.

Human: Give me a hotel in san francisco with mountain view
AI: Based on your query for a hotel in San Francisco with a mountain view, the best choice from the list provided would be the Axiom Hotel. 

The Axiom Hotel is a modern and stylish hotel located in downtown San Francisco, offering a seamless guest experience with a perfect balance of work and play. It is situated near the Powell Street Cable Car turnaround, within walking distance to Union Square shopping and dining, and steps away from public transportation options like the Powell Street BART station and Market Street trolley. 

With an impressive overall rating of 4.5, the Axiom Hotel has received positive reviews highlighting its impeccable service, modern amenities, and convenient location. Guests have praised the hotel for its exceptional staff, cleanliness, and comfort. The hotel's commitment to providing creative surprises and engaging experiences sets it apart as a unique and welcoming accommodation option in the heart of San Francisco.

While the Axiom Hotel may not offer a direct mountain view, its central location and high-quality service make it a top choice for your stay in San Francisco. The hotel's focus on technology, amenities, and personalized service align well with your preferences for a comfortable and convenient hotel experience.

Human: what's the overall rating
AI: The Axiom Hotel in San Francisco has an impressive overall rating of 4.5. This high rating reflects the positive experiences of guests who have stayed at the hotel and appreciated its impeccable service, modern amenities, and convenient location. Guests have particularly praised the exceptional staff, cleanliness, and comfort provided by the Axiom Hotel. The commitment to offering creative surprises and engaging experiences has made the hotel stand out as a unique and welcoming accommodation option in downtown San Francisco. While the hotel may not offer a direct mountain view, its central location and focus on providing a top-notch guest experience have contributed to its excellent overall rating of 4.5.

Human: what are the restaurants nearby
AI: Hey there! If you're looking for restaurants near the Axiom Hotel in San Francisco, you've got some great options to choose from. Here are a few nearby restaurants you might want to check out:

1. Cable55
2. Carl's Jr.
3. John's Grill
4. Johnny Foley's
5. Kin Khao
6. The Old Siam Thai Restaurant
7. Mo'z Cafe
8. Little Delhi

For more choices and reviews, you can explore further on TripAdvisor at this link: [Restaurants Near Axiom Hotel](https://www.tripadvisor.com/RestaurantsNear-g60713-d7624213-Axiom_Hotel-San_Francisco_California.html)

OpenTable also lists some dining options near the hotel, including places like Mastro's Steakhouse, Corzetti, and The Rotunda at Neiman Marcus. You can find more options on OpenTable here: [Restaurants Near Axiom Hotel](https://www.opentable.com/landmark/restaurants-near-axiom-hotel)

If you prefer dining within the hotel, the Axiom Hotel offers a Lounge with handcrafted drinks and small plates, as well as the Turn Cafe for casual dining and Happy Hour specials.

Just a heads up, it's a good idea to double-check with the hotel or the restaurants for the latest info on availability and operating hours. Enjoy your dining adventures in San Francisco! 🍽️🌟

Human: What are the things to do near the hotel?
AI: Hey there! If you're looking for things to do near the Axiom Hotel in San Francisco, you're in for a treat! Here are some exciting activities you can explore during your stay:

1. Experience the vibrant energy of The Castro District.
2. Take a leisurely stroll along the Embarcadero from Oracle Park to Fisherman's Wharf.
3. Hop on the world-famous cable cars accessible directly at the hotel's Powell Street entrance.
4. Visit the iconic Lombard Street for a perfect selfie moment.
5. Hike up to Coit Tower on Telegraph Hill for stunning views.
6. Explore Pier 39 with shops, restaurants, and sea lions.
7. Enjoy a picnic at Alamo Square and see the Painted Ladies.
8. Walk, bike, or drive over the Golden Gate Bridge for an unforgettable experience.
9. Discover the trendy restaurants and galleries in the Mission District.
10. Explore the Financial District with its corporate headquarters and businesses.
11. Immerse yourself in the culture of Chinatown, the oldest in the U.S.
12. Visit Fisherman's Wharf for sightseeing tours and dining.
13. Explore the ruins of the Sutro Baths, a historic site.
14. Relax at Yerba Buena Gardens, a beautiful urban oasis.
15. Take a day trip to Bolinas for coastal charm.

These activities offer a diverse range of experiences to make your stay in San Francisco memorable. Have a fantastic time exploring the city! 🌉🌟

Human: IS there any disneyland in san francisco?
AI: San Francisco does not have a Disneyland park. The nearest Disneyland park is actually located in Anaheim, California, which is about a 6-hour drive or a 1-hour flight from San Francisco. Disneyland in Anaheim is a popular destination known for its iconic attractions, entertainment, and magical experiences for visitors of all ages. If you're interested in visiting a Disneyland park, you would need to plan a separate trip to Anaheim from San Francisco. Let me know if you need any more information or assistance with your travel plans!

Human: Where is the exact address of Pier 39?
AI: The exact address of Pier 39 in San Francisco is 2 Beach Street, San Francisco, CA 94133. Pier 39 is a popular tourist destination located along the Embarcadero waterfront, offering a variety of shops, restaurants, attractions, and stunning views of the San Francisco Bay. It's a vibrant spot where visitors can enjoy shopping, dining, entertainment, and beautiful sights like the sea lions lounging on the docks. If you plan to visit Pier 39, you can easily find it by heading to 2 Beach Street in San Francisco. Enjoy your time exploring this iconic location!

Human: What are the restaurants there?
AI: Based on the chat history and your latest query about restaurants, here are some nearby dining options around the Axiom Hotel in San Francisco:

1. Cable55
2. Carl's Jr.
3. John's Grill
4. Johnny Foley's
5. Kin Khao
6. The Old Siam Thai Restaurant
7. Mo'z Cafe
8. Little Delhi

For more choices and reviews, you can explore further on TripAdvisor at this link: [Restaurants Near Axiom Hotel](https://www.tripadvisor.com/RestaurantsNear-g60713-d7624213-Axiom_Hotel-San_Francisco_California.html)

OpenTable also lists some dining options near the hotel, including places like Mastro's Steakhouse, Corzetti, and The Rotunda at Neiman Marcus. You can find more options on OpenTable here: [Restaurants Near Axiom Hotel](https://www.opentable.com/landmark/restaurants-near-axiom-hotel)

If you prefer dining within the hotel, the Axiom Hotel offers a Lounge with handcrafted drinks and small plates, as well as the Turn Cafe for casual dining and Happy Hour specials.

Feel free to explore these dining options and enjoy your culinary experiences in San Francisco! 🍽️🌟

Human: are there any other restaurants nearby other than the previous anwers?
AI: Hey there! If you're looking for more restaurant options near the Axiom Hotel in San Francisco, you're in luck! In addition to the previous suggestions, here are a few more dining spots you might want to explore:

1. Cable55
2. Carl's Jr.
3. John's Grill
4. Johnny Foley's
5. Kin Khao
6. The Old Siam Thai Restaurant
7. Mo'z Cafe
8. Little Delhi
9. Mastro's Steakhouse
10. Corzetti
11. The Rotunda at Neiman Marcus

For detailed reviews and additional choices, you can check out TripAdvisor [here](https://www.tripadvisor.com/RestaurantsNear-g60713-d7624213-Axiom_Hotel-San_Francisco_California.html) and OpenTable [here](https://www.opentable.com/landmark/restaurants-near-axiom-hotel). 

Feel free to explore these dining options and savor the culinary delights San Francisco has to offer! 🍽️🌟

Human: Are there any mexican food near hotel?           
AI: Hey there! If you're craving Mexican food near the Axiom Hotel in San Francisco, you're in luck! Here are some fantastic options to satisfy your taste buds:

1. **Californios**: Located at 355 11th St., San Francisco, Californios offers contemporary Mexican cuisine with a focus on heritage and high-quality ingredients.
   
2. **Colibri Mexican Bistro**: Situated at 438 Geary St., San Francisco, Colibri combines authentic family recipes with fresh ingredients to create delicious Mexican dishes.
   
3. **Tropisueño**: Found near the Omni San Francisco Hotel at 75 Yerba Buena Ln, San Francisco, Tropisueño serves up a variety of Mexican delights, including burritos and tacos.
   
4. **Cenote**: Located close to the Omni San Francisco Hotel at 755 Valencia St, San Francisco, Cenote delights diners with traditional Mexican flavors and ingredients.
   
5. **Uno Dos Tacos**: Situated near the Omni San Francisco Hotel at 595 Market St, San Francisco, Uno Dos Tacos offers a range of Mexican dishes, including tasty tacos and burritos.

These are just a few of the Mexican dining options near the Axiom Hotel. If you're eager for more choices or want to explore further, feel free to check out the provided URLs for additional information and reviews. Enjoy your Mexican culinary adventure in San Francisco! 🌮🇲🇽

Human: Now I changed my mind, I want to stay at San jose, is there any 3 or 4 stars hotel?
AI: Based on your preference to stay in San Jose and the available hotel options provided, the best choice for you would be the LUMA Hotel San Francisco. Although San Jose is not the same as San Francisco, the LUMA Hotel San Francisco offers a unique and modern experience that aligns with your desire for a 3 or 4-star hotel in a vibrant city setting.

The LUMA Hotel San Francisco is a brand-new hotel located in the revitalized neighborhood of Mission Bay, offering a design-forward experience that engages with the local art scene and provides hyper-local experiences. The rooftop lounge, Cavaña, offers a perfect oasis for relaxation and enjoying South American gastronomy. With an overall rating of 4.5, this hotel has received positive reviews highlighting its cleanliness, modern design, and excellent staff service.

While the other hotels like BEI San Francisco and Hotel Nikko San Francisco also have good ratings, the LUMA Hotel San Francisco stands out for its unique and trendy atmosphere, making it a great choice for a memorable stay in San Francisco.

Therefore, considering your change of mind to stay in San Jose and the available options, the LUMA Hotel San Francisco would be an excellent choice for a 3 or 4-star hotel experience that meets your preferences.

Human: How long does it take to reach san jose?
AI: Based on the chat history provided, it seems there might have been a mix-up between San Jose and San Francisco. The LUMA Hotel San Francisco was recommended based on your preference to stay in San Jose, but it is actually located in San Francisco. 

To clarify, if you are looking to reach San Jose, the travel time would depend on your starting point. If you are in San Francisco, it typically takes about 45 minutes to 1 hour to drive to San Jose, depending on traffic conditions. Alternatively, you can also consider taking public transportation options like Caltrain, which offers a convenient way to travel between the two cities.

If you need more specific information on travel times or transportation options to reach San Jose from a different location, please provide additional details so I can offer more tailored assistance.

Human: Give me a hotel in san francisco other than luma hotel
AI: Based on your query for a hotel in San Francisco other than LUMA Hotel, I recommend considering the San Remo Hotel. The San Remo Hotel offers a unique and historic boutique experience in the vibrant North Beach neighborhood, just a few blocks from Fisherman's Wharf. This family-owned hotel, built in 1906, exudes Old-World charm with specially selected antique furnishings, creating a cozy and intimate atmosphere. Each room is distinct, adding to the charm of the hotel.

The San Remo Hotel provides a sanctuary-like experience with shared baths that are meticulously cleaned daily, offering a touch of simplicity and authenticity. The absence of room telephones and televisions enhances the opportunity for a peaceful and unplugged stay. The hotel's location in North Beach, one of San Francisco's oldest and most popular areas, ensures easy access to key attractions and a unique cultural experience.

With an overall rating of 4.0 and positive reviews highlighting the hotel's charm, convenient location, and great value for money, the San Remo Hotel is a standout choice for travelers seeking a different kind of accommodation experience in San Francisco. If you appreciate history, character, and a cozy ambiance, the San Remo Hotel is a fantastic option that aligns well with your preferences.

Human: What are the activities there?
AI: There are plenty of activities near the San Remo Hotel in San Francisco! You can explore attractions like Alcatraz Island for a historic tour, visit the Asian Art Museum to immerse yourself in Asian culture, or catch a concert at the Bill Graham Civic Auditorium. If you're into science, don't miss the California Academy of Sciences with its planetarium and aquarium.

For sports and entertainment, check out the Chase Center, and for a taste of San Francisco's waterfront charm, head to Fisherman's Wharf and Ghirardelli Square for delicious treats and shopping. These spots offer a mix of history, culture, and entertainment just a stone's throw away from the San Remo Hotel. Enjoy your stay and have a fantastic time exploring the city!

Human: give me 10 places to go near the hotel
AI: Sure! Here are 10 places near the San Remo Hotel in San Francisco that you might enjoy visiting:

1. Alcatraz Island: Take a ferry to explore the historic Alcatraz Island and learn about its intriguing past as a former prison.

2. Golden Gate Park: Enjoy a day at the expansive Golden Gate Park, offering beautiful gardens, hiking trails, and recreational activities.

3. Golden Gate Bridge: Don't miss the iconic Golden Gate Bridge, a must-see landmark for stunning views and photo opportunities.

4. Twin Peaks: Visit Twin Peaks for panoramic views of the city and a scenic hike to one of the highest points in San Francisco.

5. Fisherman's Wharf: Experience the lively atmosphere of Fisherman's Wharf, where you can enjoy seafood, shopping, and picturesque views of the bay.

6. de Young Museum: Explore the exhibits and art collections at the de Young Museum, located conveniently near the San Remo Hotel.

7. Civic Center: Discover the cultural attractions at Civic Center, including the Bill Graham Civic Auditorium and other landmarks.

8. Pier 39: Visit Pier 39 for a variety of shops, restaurants, and attractions along the waterfront.

9. Asian Art Museum: Immerse yourself in Asian culture at the Asian Art Museum, located nearby for a unique cultural experience.

10. California Academy of Sciences: Explore the fascinating exhibits at the California Academy of Sciences, featuring a planetarium and aquarium for science enthusiasts.

These attractions offer a diverse range of experiences near the San Remo Hotel, ensuring you have a memorable and enjoyable stay in San Francisco!

Human: How do you go to alcatraz island?
AI: To go to Alcatraz Island from the San Remo Hotel in San Francisco, you can take a ferry from Pier 33, which is the official departure point for Alcatraz Cruises. Pier 33 is located near Fisherman's Wharf, which is within walking distance or a short drive from the San Remo Hotel. 

You can easily reach Pier 33 by various transportation options such as walking, taking a taxi, using a rideshare service, or utilizing public transportation like the Muni bus or cable car. Once you arrive at Pier 33, you can board the ferry that will take you on a scenic ride across the bay to Alcatraz Island.

It's recommended to book your tickets for the Alcatraz tour in advance, as it's a popular attraction and tickets can sell out quickly. The tour includes a captivating audio guide that provides insights into the history of the island and its former prison. Enjoy your visit to Alcatraz Island and immerse yourself in its fascinating past!

Human: based on the attraction and restaurants make me a three days itenerary 
AI: Based on the attractions and restaurants near the San Remo Hotel in San Francisco, I have crafted a three-day itinerary for you to make the most of your visit:

Day 1:
- Morning: Start your day with a visit to Alcatraz Island. Take a ferry from Pier 33 for a historic tour of the former prison.
- Afternoon: Explore the nearby Fisherman's Wharf for lunch at one of the seafood restaurants and enjoy the lively atmosphere.
- Evening: Head to Ghirardelli Square for dessert and shopping, and catch the sunset at the Golden Gate Bridge for breathtaking views.

Day 2:
- Morning: Spend the morning at Golden Gate Park, exploring the gardens, trails, and attractions like the de Young Museum.
- Afternoon: Visit the California Academy of Sciences for a fascinating experience at the planetarium and aquarium.
- Evening: Enjoy dinner at a local restaurant in the Civic Center area and attend a concert at the Bill Graham Civic Auditorium.

Day 3:
- Morning: Hike up Twin Peaks for panoramic views of the city and a scenic start to your day.
- Afternoon: Head to Pier 39 for lunch and explore the shops and attractions along the waterfront.
- Evening: Immerse yourself in Asian culture at the Asian Art Museum and end your day with a relaxing dinner at a nearby restaurant.

This itinerary combines a mix of historical sites, cultural experiences, and culinary delights near the San Remo Hotel, ensuring you have a diverse and memorable three-day stay in San Francisco. Enjoy your time exploring the city!# rag-hotel-data
