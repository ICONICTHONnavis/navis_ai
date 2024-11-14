from .models import complete_tb, subject_tb
from .serializers import recommendSerializer
from user.models import user_tb

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from .template import gen_nl_template
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def gen_desc(user_id):
    complete_subject = complete_tb.objects.filter(user_id=user_id).values()
    data = []
    for i in complete_subject:
        subject_name = subject_tb.objects.get(id=i['subject_id']).name
        data.append(
            {
                "grade": i["grade"],
                "subject_name": subject_name,
                "semester": i["semester"],
            }
        )
        # data = i["grade"] + " | " + subject_name + " | " + i["semester"]
    llm = ChatOpenAI(temperature=0.0,  # 창의성 (0.0 ~ 2.0)
                     max_tokens=2048,  # 최대 토큰수
                     model_name='gpt-4o',  # 모델명
                     )
    memory = ConversationBufferMemory()
    system_message = SystemMessage(content=gen_nl_template)
    human_message = HumanMessagePromptTemplate.from_template("current content: {history}, <data>: {input}")
    user_prompt = ChatPromptTemplate(messages=[system_message, human_message])
    conversation = ConversationChain(
        prompt=user_prompt,
        llm=llm,
        memory=memory,
    )
    return conversation.invoke(str(data))["response"]