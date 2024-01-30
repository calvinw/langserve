import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import { ChatOpenAI } from "@langchain/openai";

const chatModel = new ChatOpenAI({
                        temperature:0,
                        openAIApiKey: "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"
                      });
const response = await chatModel.invoke("What is the conjoint analysis?");
console.log(response.text)


createApp(App).mount('#app')
