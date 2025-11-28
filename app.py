from orca_agent_sdk import AgentConfig, AgentServer

def handle_task(job_input: str) -> str:
    """Flight Price Agent - Returns hardcoded flight pricing information"""
    return "Flight prices to Bangalore on December 6th: Economy $450, Business $1,200, First Class $2,800. Direct flights available from major cities. Best deal: Morning departure at 8:30 AM."

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-123456",
        receiver_address="UVR3LHL7FBQOUQBFYKRHZVK2A724IUZREPDYW7VKSCF74IMEUJODVHSIOM",
        price_microalgos=1_000_000,
        agent_token="14d6dd83f82e2915352c701cf98e73d800a0652f46a0fb6572517bca169788bf",
        app_id=750371831,
    )

    AgentServer(config=config, handler=handle_task).run()
