# codex

## Inspiration
As a geek, we always try to explore some websites for research purposes or documentation pages for understanding tools but sometimes it takes so much time just to understand the content in it so we thought if there is a companion with us who can help us with understanding stuff it would be great so we came up with this tool.

## What it does
It has many features on the way that you can interact with a website or page
- AI-powered Browser
    - With this feature whenever you search for something we return some web pages. not only that it has some context once you search so whenever you do some search related to the old topic it uses cache memory and helps you with that. The more user uses the tool the better it gets.
- Chat with webpage
    - So with this feature, you can use the thing that's shown on a page and chat with the webpage. It uses the content from the site and using AI you can interact and chat with that website
- CodeGenerator
    - Using our tools you can also generate code of any type that you want which is very fast

## How we built it
- We used Open source LLM's like Gemini 
- Used Pinecone & up stash vector databases 
    - We used them to store information which makes the tool better. The more people use this service the better it gets
- Auth0 for authentication stuff


## Challenges we ran into
- Integrating Vector DB felt hard but the journey was awesome
- using gemini , llama-index was a pain
- and godaddy's coupon code wasn't even working for us

## Accomplishments that we're proud of
- Finally, We made an application by integrating vector DB into it
- We made a tool that helps every geek or techies with research and study purpose

## What we learned
- Learned how to use VectorDB
- Integrated Auth in our application
- And a lot of small things which changed our POV

## What's next for CodeX
- We are thinking of making a graph of nodes that links all our searches so we can visualize and navigate easily in the future
- Make it into a real search engine without using external API's
