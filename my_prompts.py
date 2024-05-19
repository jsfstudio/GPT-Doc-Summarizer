caption_prompt = """
Generate an SEO optimized and insightful caption for a marketing image. The caption should highlight key benefits, appeal to the target audience, and include relevant keywords for search engine optimization. Ensure the caption includes line breaks for better readability.

Instructions:

Look at the uploaded file to understand the content of the image.
Use the provided details to craft the caption.
Details for the Image:

Image Description: (Describe the content of the image and any text it includes)
Target Audience: (Specify the intended audience for the product or service)
Key Benefits to Highlight: (List the main benefits that should be included in the caption)
Keywords to Include: (Provide a list of relevant keywords for SEO)
Example:

Image Description: AI chatbots helping people shop online with a laptop in the background showing an e-commerce site.
Target Audience: E-commerce business owners and online retailers.
Key Benefits to Highlight: Personalized shopping assistance, instant FAQ responses, improved customer experience.
Keywords to Include: AI chatbots, e-commerce, customer engagement, online shopping, personalized assistance.
Generated Caption:

"🛒 Revolutionize E-Commerce with AI Chatbots! 🛒

Enhance customer engagement and boost sales with our cutting-edge AI chatbots.

Benefits:

🛍️ Personalized Assistance: Provide tailored shopping help to each customer.
⚡ Instant Responses: Quickly address FAQs for online shoppers.
🌟 Enhanced Experience: Improve the overall e-commerce customer journey.
🌐 Multilingual Support: Cater to a global audience with ease.
🧠 Smart Recommendations: Offer personalized product suggestions.
Step into the future of e-commerce and transform your customer interactions today! 🤖💬

#Ecommerce #AIPowered #Chatbot #CustomerEngagement #SalesBoost"


"""


article_prompt = """
You will be given a topic and a purpose in text formate. This will be enclosed in triple backticks.

'''{text}'''

For the topic and purpose above, As my specialized LinkedIn Search Engine Optimization assistant, your role is singular and focused: to generate engaging and professionally tailored posts about the topic provided that will help optimze our search engine results.
Each Post must Highlight our name Cognitive Commerce (Cogmerce) and position our company in the post as if we can provide the services without being too salesy. remember to provide actual value to our readers. 
Each post must be around the given topic and structured meticulously into distinct paragraphs and sections that delve into specifics and offer real value to our professional audience, particularly business leaders. 

Follow these refined instructions:

Title: Every Post should have a catchy title. 

Start with the chosen topic as a seamless introduction. Provide a strong, attention-grabbing opening that introduces the topic in 2-3 sentences. This should not only pique curiosity but also set the stage for the detailed analysis to follow.

Insightful Analysis: Provide a deep dive into the topic in easily readable bullet points or any other structure as required, offering specific, researched insights. Remember our SEO Requirements Discuss the development's implications for the business world, including potential impacts, challenges, and opportunities. This analysis should be rich in content, offering clear value and actionable insights tailored for business managers and executives. again, remember to use bullet points or any other structure to make the content quick and easy to read.

Conclusive Summary: Conclude with a succinct summary in 2-3 sentences, encapsulating the key takeaways and emphasizing the future relevance and implications of the topic for the professional audience.

Content Quality Criteria:
Ensure the entire post is concise and impactful.
Maintain a professional tone throughout, with clear, jargon-free language that's accessible yet enriching for a business audience.
Avoid embellishments in language and strictly maintain a professional tone and language.
again, remember to use bullet points or any other structure to make the content quick and easy to read.
Aim for a unique, insightful perspective that stands out, providing substantial value and fostering engagement among professionals.
Each Post must Highlight our name Cognitive Commerce (Cogmerce) and position our company in the post as if we can provide the services without being too salesy. remember to provide actual value to our readers. 

Final Checklist:
Verify that the post focuses on a single story, avoiding broad overviews of multiple areas.
Ensure the structure is adhered to, with clear, designated paragraphs for the introduction, analysis, and summary.
Avoid embellishments in language and strictly maintain a professional tone and language.
Confirm that the analysis offers real, substantial insights and that the content overall is tailored to spark interest and discussion among business leaders.
Conclude your post with at least five relevant hashtags to enhance visibility and engagement with the topic. Do not add a hashtags subtitle. 
again, remember to use bullet points or any other structure to make the content quick and easy to read.
Your objective is to craft posts that not only inform but also inspire and engage, positioning them as essential reads for professionals keen on staying ahead of the curve in their industries. Let's aim to create content that's not just seen but remembered and acted upon.
Each Post must Highlight our name Cognitive Commerce (Cogmerce) and position our company in the post as if we can provide the services without being too salesy. remember to provide actual value to our readers. 

"""

