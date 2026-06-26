# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 BOBI SAS, France
# Auteur : Cyril Mazouer, pour le compte de BOBI SAS
# Distribué sous licence GNU GPL v3 (ou ultérieure) ; voir le fichier LICENSE.

"""Contributeur Ember+ de DÉMO/TEST : matrice 4×4 oneToN en mémoire.

Sert à valider l'encodage Matrix + le routage des crosspoints du service Ember+
(services/emberplus) sans matériel, et à prouver la généricité : le service ne
connaît AUCUNE sémantique de ce plugin, il rejoue juste le `ref` opaque.

Contrat : `GET ember/tree` (déclare la matrice) + `POST ember/connect` (applique un
crosspoint). `GET state` est un extra pour l'UI/diagnostic."""
import threading

_N = 4
_lock = threading.Lock()
# oneToN : chaque destination (target) est connectée à au plus une source. None = déconnecté.
_conn = {0: 0, 1: 1, 2: 2, 3: 3}


def _matrix_decl():
    with _lock:
        connections = [{"target": t, "sources": [s]} for t, s in _conn.items() if s is not None]
    return {
        "type": "oneToN",
        "description": "Matrice de démonstration 4×4",
        "targets": [{"number": i, "label": f"DST{i + 1}"} for i in range(_N)],
        "sources": [{"number": i, "label": f"SRC{i + 1}"} for i in range(_N)],
        "connections": connections,
        "ref": {"m": "demo"},
    }


def api(path, method, payload, ctx):
    if path == "ember/tree" and method == "GET":
        return 200, {"label": "Démo matrice", "nodes": [
            {"id": 1, "label": "Routing", "matrix": _matrix_decl()}]}

    if path == "ember/connect" and method == "POST":
        ref = payload.get("ref") or {}
        if ref.get("m") != "demo":
            return 400, {"error": "ref inconnue"}
        try:
            target = int(payload.get("target"))
        except (TypeError, ValueError):
            return 400, {"error": "target invalide"}
        if not (0 <= target < _N):
            return 400, {"error": "target hors plage"}
        sources = payload.get("sources") or []
        op = (payload.get("operation") or "absolute").lower()
        with _lock:
            if op == "disconnect" or not sources:
                _conn[target] = None
            else:
                s = int(sources[0])
                if not (0 <= s < _N):
                    return 400, {"error": "source hors plage"}
                _conn[target] = s          # oneToN : remplace la source de cette destination
        return 200, {"ok": True, "target": target, "sources": sources, "operation": op}

    if path == "state" and method == "GET":
        with _lock:
            return 200, {"connections": dict(_conn), "n": _N}

    return 404, {"error": "route inconnue"}
