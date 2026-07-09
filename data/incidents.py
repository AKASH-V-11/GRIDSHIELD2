import datetime
import uuid

# -------------------------------
# In-memory Incident Database
# -------------------------------

INCIDENT_DB = []


def add_incident(fault, severity, affected, action):
    """
    Add a new incident to the database.
    """

    incident = {
        "id": str(uuid.uuid4())[:8],
        "time": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "fault": fault,
        "severity": severity,
        "affected": affected,
        "action": action,
        "status": "ACTIVE"
    }

    INCIDENT_DB.append(incident)

    return incident


def get_incidents():
    """
    Return all incidents.
    """
    return INCIDENT_DB


def resolve_incident(incident_id):
    """
    Mark an incident as RESOLVED.
    """
    for incident in INCIDENT_DB:
        if incident["id"] == incident_id:
            incident["status"] = "RESOLVED"
            return True

    return False


def clear_incidents():
    """
    Remove all incidents.
    """
    INCIDENT_DB.clear()


def total_incidents():
    """
    Return total number of incidents.
    """
    return len(INCIDENT_DB)


def active_incidents():
    """
    Return only ACTIVE incidents.
    """
    return [i for i in INCIDENT_DB if i["status"] == "ACTIVE"]


def resolved_incidents():
    """
    Return only RESOLVED incidents.
    """
    return [i for i in INCIDENT_DB if i["status"] == "RESOLVED"]