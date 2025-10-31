
# Index
1. [[#What is MCP]]
	- [[#Key characteristics]]
2. [[#Why was MCP introduced?]]
	- [[#The problem context]]
	- [[#What MCP addresses]]
3. [[#Who introduced MCP (and adoption)]]
4. [[#Functionality, Architecture & Key Components]]
	- [[#High-level architecture]]
	- [[#Message / transport model]]
	- [[#Functional capabilities]]
	- [[#Example usage]]
		- [[#Benefits]]
5. [[#Current Challenges]]
	- [[#Security & Safety Risks]]
	- [[#Ecosystem Maturity, Standardization & Interoperability]]
	- [[#Performance, Scaling and Cost]]
	- [[#Contextual Correctness, Governance & Reliability]]
6. [[#Summary]]
7. [[#Other Sources]]

# What is MCP

The **Model Context Protocol (MCP)** is an open-standard protocol and framework designed to enable large language models (LLMs) and other AI systems to connect, share, and act upon external tools, data sources, context objects and services in a standardized way.
## Key characteristics:

- Acts as a unified integration layer between AI systems (hosts/clients) and various external resources (servers/tools). 

- Provides a protocol definition (message formats, transports, types of operations) so that different systems can interoperate rather than each building separate bespoke connectors. 

- Enables “context” to become a first‐class citizen: not just prompts, but structured access to tools, data, memory, workflows via a common format. 

# Why was MCP introduced?

## The problem context

- As AI systems became more agentic (i.e., using tools, interacting with services, doing actions beyond pure text generation), each integration (LLM → database, LLM → web search, LLM → cloud files) required custom engineering: custom API wrappers, bespoke connectors, proprietary flows.

- This “N × M” problem is often cited: if you have N models/agents and M data sources/tools, building N×M unique integrations is costly, error-prone and not scalable.

- Further, traditional LLMs remained largely stateless or limited: they could answer from training data, but lacked structured access to live context, to tool calls, to memory, and to inter‐component coordination.

## What MCP addresses

- Provides a common, ***plug-and-play integration layer***, so that each AI application doesn’t have to build custom integration layer for each tool/data source. That reduces engineering overhead and increases reuse.

- Supports ***real-time access*** and ***contextual embedding*** of external data sources and tools into AI workflows (rather than just pre-ingested documents).

- Helps make AI systems more ***modular, composable, and auditable***: you can treat context and tool capabilities as services exposed via MCP Servers, with standard interactions.

- Improves ***interoperability***: multiple AI hosts/clients can use MCP servers, and servers built once can serve many clients. This fosters ecosystem growth.

Hence MCP was introduced to push AI systems from isolated, bespoke tool integrations toward a more open, standard-based architecture that can scale.

# Who introduced MCP (and adoption)

- The protocol was ***introduced by Anthropic*** (an AI research & product company) in ***November 2024***.

- After its release as an open-source / open-standard framework, it gained adoption by major players: e.g., OpenAI announced adoption in early 2025; Google DeepMind also committed support.

- The framing in media: many describe MCP as the “USB-C of AI apps” because it serves as a universal connector/interface.

- Research papers are now studying MCP implementations, security issues, ecosystem health. For example: [“Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers”](https://arxiv.org/abs/2506.13538).

Thus MCP is a relatively recent but rapidly spreading standard in the AI-agent/tool ecosystem.

# Functionality, Architecture & Key Components

## High-level architecture

According to documentation, MCP uses a ***host / client / server model***.

- ***MCP Host:*** The AI application or agent environment (for instance an LLM-based assistant) that wants to use tools/data.

- ***MCP Client:*** The component inside the host that manages the protocol communication with servers; each client connects to one MCP server.

- ***MCP Server:*** Exposes resources, tool capabilities, context, prompts etc via the MCP interface; it is what the client talks to.

## Message / transport model

- MCP defines message formats (often using JSON-RPC 2.0) and transports (stdin/stdout or HTTP/SSE) for how client and server communicate.

- The protocol includes operations such as tool invocation, resource lookup, prompt template execution, context retrieval, updates, etc.

## Functional capabilities

- ***Discovery:*** MCP allows a host to discover what tools/resources a server offers.

- ***Invocation:*** The AI (via client) can invoke tools/actions on server (e.g., query a database, execute a function, interact with a cloud service).

- ***Context provisioning:*** The server can provide structured context (files, metadata, prompts, memory) to the AI model, enabling richer responses and tool usage.

***Managing state:*** MCP supports managing session, context updates, tool chaining, and stateful workflows—not just one‐off prompts.

***Security/access control:*** The protocol supports permissioning, authorization and auditability of tool/data access.

## Example usage

Suppose you have an AI assistant which needs to query a CRM database for customer info, then write an email via Gmail API:

- You build a MCP server for the CRM exposing query tools.

- A MCP server for Gmail exposing “send email” action.

- The assistant (host) runs a client to each server, invokes the CRM tool, gets data, then invokes Gmail tool.

- The interactions are standardized, the host doesn’t need custom code per tool, and context (customer record, company policy etc) is passed in a structured way.
### Benefits

- Reduced integration burden (one protocol vs many custom APIs).

- More modular AI agent architecture (separate host logic, client connectors, server implementations).

- Better scalability and maintainability.

- Improved observability, security and standardization across the AI-tool ecosystem.

# Current Challenges

While MCP offers significant promise, the research and practitioner community recognize a number of open issues and future challenges.

## Security & Safety Risks

- Studies show that MCP, being flexible and powerful, opens new attack surfaces. For example, ***tool-poisoning, unauthorized tool invocation, context manipulation, credential-leak risks***. ([Source](https://arxiv.org/abs/2504.03767))

- Identity fragmentation remains a major vulnerability: many MCP servers run with weak auth, fragmented identity across systems, making it easier for attackers to exploit.

- Because MCP enables agents to execute actions (not just read data), the potential for malicious code execution is real; researchers highlight need for safety auditing (e.g., MCP SafetyScanner) and stricter controls. ([Source](https://arxiv.org/abs/2504.03767))

## Ecosystem Maturity, Standardization & Interoperability

- Although MCP provides standards, there’s still variation in implementations, dialects, transports, and schemas. Some servers may deviate from spec or have limited support for certain features (e.g., bidirectional notifications). > Example quote from reddit: “A native transport layer, enabling MCP servers to be embedded… still missing”. ([Source](https://www.reddit.com/r/modelcontextprotocol/comments/1l78ocs))

- Measurement studies show many listed MCP projects are low quality, poorly maintained or sidelined. The ecosystem is still in transitional phase. ([Source](https://arxiv.org/abs/2509.25292))

- Ensuring compliance, versioning, backward compatibility, and governance of the standard are ongoing concerns.

## Performance, Scaling and Cost

- Real-time, tool-rich, context-rich AI workflows can be heavy: maintaining state, managing many servers, context switching, security checks all add latency and cost.

- If an AI agent calls many tools/components via MCP, orchestration becomes complex. Ensuring predictable performance is non-trivial.

## Contextual Correctness, Governance & Reliability

- While MCP provides access to external data/tools, the quality of the context, memory, tool output and how the model uses it is still a research challenge. ***Garbage in → Garbage out***.

- Governance issues: Which context should the AI have access to? How to enforce data‐privacy, audit trails, user consent? MCP gives the mechanism but policy remains.

- Model behaviour: The AI must still choose which tool to call, interpret the output correctly, incorporate it in its reasoning. MCP doesn’t solve the “agent decision making” problem entirely; it supplies infrastructure.

# Summary

- ***Definition:*** MCP is an open standard protocol for connecting AI systems (hosts/clients) with external tools/data (servers) in a unified way.

- ***Motivation:*** Solve the integration explosion (N×M) of bespoke connectors and enable richer, context-aware, tool-enabled AI agents.

- ***Origin & adoption:*** Introduced by ***Anthropic in Nov 2024***; adopted by major players (OpenAI, Google DeepMind, Microsoft) in 2025.

- ***Core components:*** Host, Client, Server; message/transport spec; discovery, invocation, context provisioning capabilities.

- ***Benefits:*** Faster integration, modular agent design, interoperability, improved observability and security (in theory).

- ***Limitations / Challenges:*** Security (tool poisoning, identity fragmentation), ecosystem maturity, performance/cost, governance and standard evolution.

- ***Future Outlook:*** MCP may become foundational to the “agentic web” of AI, enabling interoperable, context-rich agents and tools—but its full potential depends on addressing the outstanding issues.

# Other Sources

- [All You Need To Know About Model Context Protocol(MCP) | Krish Naik](https://www.youtube.com/watch?v=-UQ6OZywZ2I)
