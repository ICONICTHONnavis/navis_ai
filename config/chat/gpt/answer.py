from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from .template import default_template
from langchain_core.messages import SystemMessage
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from chat.models import chat_tb

def chat_answer(chattingQuestion, user_id, user_template):
    history = get_history_tuple(user_id)
    llm = ChatOpenAI(temperature=0.0,  # 창의성 (0.0 ~ 2.0)
                     max_tokens=2048,  # 최대 토큰수
                     model_name='gpt-4o',  # 모델명
                     )
    memory = ConversationBufferMemory()
    for i in history:
        memory.save_context({"input": i["input"]},
                            {"outputs": i["outputs"]})
    system_message = SystemMessage(content=default_template + user_template)
    human_message = HumanMessagePromptTemplate.from_template("current content: {history}, <question>: {input}")
    user_prompt = ChatPromptTemplate(messages=[system_message, human_message])
    conversation = ConversationChain(
        prompt=user_prompt,
        llm=llm,
        memory=memory,
    )
    return conversation.invoke(chattingQuestion)["response"]

def get_history_tuple(user_id):
    try:
        chat_data = chat_tb.objects.filter(user_id=user_id).values()
        history = []
        if (len(chat_data) == 0):
            return ""
        for i in chat_data:
            history.append({"input": i['question'], "outputs": i['answer']})
        return history
    except chat_tb.DoesNotExist:
        return []