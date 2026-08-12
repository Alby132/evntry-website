// Minimal Cloudflare Worker — serves all requests from the static assets bundle
export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  },
};
