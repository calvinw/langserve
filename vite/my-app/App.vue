<template>
  <div id="app">
    <textarea v-model="text" placeholder="Enter text here" />
    <button @click="submit">Submit</button>
    <div v-if="htmlContent" class="html-content" v-html="htmlContent"></div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const text = ref('');
    const htmlContent = ref(null);

    const submit = async () => {
      // const apiResponse = await fetch('/api/endpoint', {
      //   method: 'POST',
      //   body: JSON.stringify({ text: text.value }),
      // });
      //
      // const htmlUrl = await apiResponse.json();
      //
      // const htmlResponse = await fetch(htmlUrl);
      // const html = await htmlResponse.text();

      htmlContent.value = text.value;
    };

    return { text, htmlContent, submit };
  },
};
</script>
