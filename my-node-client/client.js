
console.log("client begins XXXXXXX")

import { RemoteRunnable } from "langchain/runnables/remote";

let chain = null;
let result = null;

// console.log("calling llm_chain:")
// chain = new RemoteRunnable({
//   url: "http://localhost:8000/llm/"
// });
// result = await chain.invoke(
//   "What is 4+2?"
// );
// console.log(result.content)


console.log("calling z_value_params_chain:")
chain = new RemoteRunnable({
  url: "http://localhost:8000/z_value_params/"
});

result = await chain.invoke({text: "This is a problem where we want to find the z-value for a normal curve and a given x-value. Suppose that x is -223.3, the mean is -2.300000, and standard deviation is .443. What is the z-value?"});
console.log(result.content)

console.log("client ends YYYYYY")
