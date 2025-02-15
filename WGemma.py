from llama_cpp import Llama
from finals import final_dict

llm = Llama.from_pretrained(
  repo_id="DavidAU/Gemma-The-Writer-N-Restless-Quill-10B-Uncensored-GGUF",
  filename="Gemma-The-Writer-N-Restless-Quill-10B-D_AU-IQ4_XS.gguf",
)

response_dict = {}
for key, value in final_dict.items():
    response = llm.create_chat_completion(
    messages = [
		{
			"role": "user",
			"content": f"Exhibiting conversational flow, contextual awareness, vivid description, humor and an appropriate level nauce, write the non-fiction prose variant of the following using the contextual terms in square brackets as suggestive modifiers while maintaining word count: \n\n{value}"
		}
    ]
    )
    response_dict[key] = response
	
	
with open("results.txt", "w") as file:
   for key, value in response_dict.items():
       print(value, file=file)
       print("\n\n\n", file=file)
       
       
   
