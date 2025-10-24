import os, uuid, boto3

region = os.getenv("AWS_REGION", "us-east-1")
agent_id = os.getenv("AGENT_ID")
alias_id = os.getenv("AGENT_ALIAS_ID")

assert agent_id and alias_id, "Faltan AGENT_ID o AGENT_ALIAS_ID"

rt = boto3.client("bedrock-agent-runtime", region_name=region)

resp = rt.invoke_agent(
    agentId=agent_id,
    agentAliasId=alias_id,
    sessionId=str(uuid.uuid4()),
    inputText="¿Qué es SageMaker JumpStart?",
    enableTrace=False,
    endSession=False,
)

out = []
for ev in resp.get("completion", []):
    if "chunk" in ev:
        out.append(ev["chunk"]["bytes"].decode("utf-8", errors="ignore"))

print("\n=== RESPUESTA ===\n", "".join(out).strip() or "(vacío)")
