// SPDX-License-Identifier: GPL-3.0-or-later
// Contributeur de test : affiche l'état des connexions de la matrice de démo.
window.BTTools = window.BTTools || {};
window.BTTools["ember_matrix_demo"] = {
  async mount(el, ctx) {
    const load = async () => {
      try {
        const d = await ctx.api("state");
        const lines = Object.entries(d.connections)
          .map(([t, s]) => `DST${(+t) + 1} ← ${s === null ? "—" : "SRC" + ((+s) + 1)}`);
        el.querySelector("#emd-state").textContent = lines.join("\n");
      } catch (e) {
        el.querySelector("#emd-state").textContent = "Erreur : " + e.message;
      }
    };
    el.querySelector("#emd-refresh").onclick = load;
    await load();
  },
  unmount() {}
};
