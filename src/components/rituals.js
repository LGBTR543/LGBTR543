const { OpenAI } = require('openai');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function generateRitual(prompt = '') {
  const completion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: `Describe a mystical ritual for ${prompt}` }],
    model: 'gpt-3.5-turbo'
  });
  return completion.choices[0].message.content.trim();
}

module.exports = { generateRitual };
