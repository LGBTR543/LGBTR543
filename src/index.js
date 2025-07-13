const express = require('express');
const { generateLyrics } = require('./components/lyrics');
const { generateSlogan } = require('./components/slogans');
const { generateRitual } = require('./components/rituals');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(express.static('public'));

app.post('/api/generate', async (req, res) => {
  const { type, prompt } = req.body || {};
  try {
    let result;
    switch (type) {
      case 'lyrics':
        result = await generateLyrics(prompt);
        break;
      case 'slogan':
        result = await generateSlogan(prompt);
        break;
      case 'ritual':
        result = await generateRitual(prompt);
        break;
      default:
        return res.status(400).json({ error: 'Invalid type' });
    }
    res.json({ result });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`JuankoOS listening on port ${port}`);
});
