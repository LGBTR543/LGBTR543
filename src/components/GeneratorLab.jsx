import { useState } from 'react';

const modes = [
  { id: 'lyrics', label: 'Lyrics Generator' },
  { id: 'slogans', label: 'Signal Slogans' },
  { id: 'rituals', label: 'Ritual Activator' }
];

const prompts = {
  lyrics: 'Write 8 lines of mystical futuristic lyrics for an underground artist awakening their signal.',
  slogans: 'Create 10 short premium slogans for ALTO SABOTAJE™ and JuankoOS™ in Spanish + English.',
  rituals: 'Design a 5-step symbolic ritual for creators to break sabotage patterns and enter flow.'
};

export default function GeneratorLab() {
  const [mode, setMode] = useState('lyrics');
  const [input, setInput] = useState('Tema: transformación espiritual con estética noir-violeta.');
  const [output, setOutput] = useState('Awaiting transmission...');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async (event) => {
    event.preventDefault();
    setLoading(true);

    try {
      if (!import.meta.env.VITE_OPENAI_API_KEY) {
        setOutput(
          'OpenAI key not detected. Add VITE_OPENAI_API_KEY to enable live generation. Placeholder mode active.'
        );
        return;
      }

      const response = await fetch('https://api.openai.com/v1/responses', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`
        },
        body: JSON.stringify({
          model: 'gpt-4.1-mini',
          input: `${prompts[mode]} Context: ${input}`
        })
      });

      const data = await response.json();
      const text = data?.output?.[0]?.content?.[0]?.text || 'Signal received, but no text payload returned.';
      setOutput(text);
    } catch (error) {
      setOutput(`Transmission error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="juankoos" className="rounded-2xl border border-amber-500/20 bg-zinc-950/80 p-6">
      <p className="text-xs uppercase tracking-[0.3em] text-amber-300">JuankoOS™ / Creative Oracle</p>
      <h3 className="mt-2 text-2xl font-semibold">Assistant for lyrics, slogans, and rituals.</h3>
      <p className="mt-2 text-sm text-zinc-400">Modular prompt engine ready for OpenAI API, memberships, and digital product pipelines.</p>

      <div className="mt-5 flex flex-wrap gap-2">
        {modes.map((item) => (
          <button
            key={item.id}
            onClick={() => setMode(item.id)}
            className={`rounded-full px-4 py-2 text-xs ${mode === item.id ? 'bg-violet text-white' : 'border border-zinc-700 text-zinc-300'}`}
          >
            {item.label}
          </button>
        ))}
      </div>

      <form className="mt-5 space-y-4" onSubmit={handleGenerate}>
        <label className="block text-sm text-zinc-300">
          Input transmission
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="mt-2 h-28 w-full rounded-lg border border-zinc-700 bg-black p-3 text-sm"
          />
        </label>
        <button className="rounded-lg bg-amber-300 px-4 py-2 text-sm font-semibold text-black" type="submit">
          {loading ? 'Generating...' : 'Generate signal'}
        </button>
      </form>

      <pre className="mt-4 whitespace-pre-wrap rounded-xl border border-zinc-800 bg-black p-4 text-xs text-zinc-300">{output}</pre>
    </section>
  );
}
