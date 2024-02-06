<template>
  <div id="app">
    <textarea v-model="text" placeholder="Enter text here" />
    <button @click="submit">Submit</button>
    <div v-if="htmlContent" class="html-content" v-html="htmlContent"></div>
  </div>
</template>

<script>
import { ref, nextTick } from 'vue';
import { RemoteRunnable } from "langchain/runnables/remote";

export default {
  setup() {
    const text = ref('');
    const htmlContent = ref(null);

    const submit = async () => {

      const remoteChain = new RemoteRunnable({
        url: "http://localhost:8000/gemini"
      });
      const result = await remoteChain.invoke({
        "input": text.value
      });

      console.log(result.content)

      const urlBase = ""
      //const params = "NormalLeftTail?mu=30&sigma=4&x=25"
      const url = urlBase + result.content

      const htmlResponse = await fetch(url);
      const html = await htmlResponse.text();
      htmlContent.value = html;

      await nextTick()
      MathJax.typeset();
    };

    return { text, htmlContent, submit };
  },
};
</script>
