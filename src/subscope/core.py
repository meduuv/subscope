from __future__ import annotations

import socket
from dataclasses import dataclass


@dataclass(frozen=True)
class Host:
    name: str
    addresses: tuple[str, ...]


def normalize(domain: str) -> str:
    domain = domain.strip().lower().rstrip(".")
    if not domain or any(ch.isspace() for ch in domain):
        raise ValueError("invalid domain")
    return domain


def resolve(name: str) -> Host:
    name = normalize(name)
    try:
        infos = socket.getaddrinfo(name, None)
    except OSError:
        return Host(name, ())
    addresses = tuple(sorted({item[4][0] for item in infos}))
    return Host(name, addresses)
