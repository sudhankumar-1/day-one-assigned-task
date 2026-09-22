# Agentic AI: Foundations and Open-Source Practice
## Day 1 Task - Comparing Approaches

### 3.1 Explanation of each approach

#### Plain Chatbot
The plain chatbot approach relies entirely on a Large Language Model (LLM) without any external tools or data access. It takes the user's query and generates a response based purely on its pre-trained knowledge. It does not use any private data, and it cannot access the local `expenses.csv` file. There are no tools or rules involved; it just provides a text completion based on the prompt. From start to finish, the chatbot receives the user's request ("How much did I spend on food this month?"), processes it through the LLM, and returns a general or hallucinated response because it doesn't know the user's actual spending. Its limitations are obvious in this scenario: it cannot provide factual answers about private or dynamic data since it has no way to retrieve it.

#### Rule-Based Workflow
The rule-based workflow is a deterministic Python script that follows predefined steps and conditions to answer the query, without involving an LLM. It uses the `expenses.csv` private data file. It does not require any external AI tools but relies on strict programmed rules (e.g., searching for keywords like "how much", "spend", and "food"). When it receives the user's request, it checks if the request matches its programmed keywords. If a match is found, it opens the CSV, filters for the requested category, calculates the total, and returns the result. Its limitations appear when the user phrases their request differently (e.g., "What were my dining costs?") or asks for something not explicitly coded (e.g., "What did I spend on transport on October 2nd?"), as it will fail to understand the query due to its rigid keyword-matching nature.

#### AI Agent
The AI agent approach combines an LLM with a Tool and a reasoning Loop. It uses the `expenses.csv` private data file by utilizing a custom tool called `read_expenses_csv`. From start to finish, the agent receives the user's query, reasons that it needs to check the user's expenses to answer accurately, and decides to call the `read_expenses_csv` tool. The tool executes, reads the local file, and returns the data to the agent. The agent then observes the data, performs the necessary calculation (summing the food expenses), and formulates a final, accurate response. Its limitations might appear if the data file is extremely large (exceeding context limits) or if the agent makes a mistake in its reasoning, though it is far more capable than the plain chatbot.

### 3.2 Comparison table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
| :--- | :--- | :--- | :--- |
| **Flexibility** | High (can talk about anything, but generally) | Low (only handles specific, pre-programmed phrasing) | High (can understand natural language variations and adapt) |
| **Decision-making** | Minimal (just predicts next words) | Rigid (uses explicit if/else conditions) | Advanced (reasons about which tool to use and when) |
| **Tool usage** | None | None (uses standard code logic) | Yes (can invoke external functions/tools) |
| **Private-data access** | None | Yes (hardcoded file access) | Yes (via tools it decides to call) |
| **Multi-step task handling** | No (single prompt/response) | Limited (only if explicitly programmed) | Yes (can loop through thought, action, and observation) |
| **Automation** | None | High for specific tasks | High, adaptable automation |
| **Reliability** | Low for factual private data | High (but fragile to input variations) | High (can verify and correct itself based on tool output) |

### 3.3 Suitability analysis

For this personal expense tracker scenario, the **AI agent** is the most suitable approach. The scenario requires accessing private, dynamically updated data (which rules out the plain chatbot) and dealing with natural, flexible user queries (which the rule-based workflow struggles with). The AI agent provides the perfect balance by leveraging the LLM's natural language understanding to interpret the user's intent, while using the tool to fetch the required factual data. It is reliable enough to give accurate calculations based on the CSV and flexible enough to handle variations like "food costs", "dining expenses", or "how much did I pay for groceries".

### 3.4 Conclusion

In general, a **plain chatbot** is the most appropriate choice for general knowledge inquiries, creative writing, or brainstorming where private factual data is not needed. A **rule-based workflow** is ideal for highly predictable, repetitive, and mission-critical tasks where the inputs are structured, and you need 100% deterministic and extremely fast execution without the cost of an LLM. An **AI agent** shines when the problem involves unstructured inputs (natural language), requires access to external or private data, and involves complex, multi-step reasoning where the system must autonomously decide how to achieve the goal using available tools.
