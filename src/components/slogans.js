const { OpenAI } = require('openai');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function generateSlogan(prompt = '') {
  const completion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: `Create a short, catchy slogan for ${prompt}` }],
    model: 'gpt-3.5-turbo'
  });
  return completion.choices[0].message.content.trim();
}

module.exports = { generateSlogan };
