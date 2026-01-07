import { useEffect, useState } from "react";

const API = "http://IP_KOMPUTER_KAMU:5000";

export default function App() {
  const [sensor, setSensor] = useState({});
  const [control, setControl] = useState({});

  const fetchData = async () => {
    const s = await fetch(API + "/api/sensor").then(res => res.json());
    const c = await fetch(API + "/api/control").then(res => res.json());
    setSensor(s);
    setControl(c);
  };

  const setMode = async (mode) => {
    await fetch(API + "/api/control", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mode })
    });
    fetchData();
  };

  const setLamp = async (lamp) => {
    await fetch(API + "/api/control", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lamp, mode: "MANUAL" })
    });
    fetchData();
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Smart Lamp IoT Dashboard
      </h1>

      <div className="grid md:grid-cols-3 gap-4 mb-6">
        <Card title="PIR Sensor" value={sensor.pir ? "Motion" : "No Motion"} />
        <Card title="LDR Value" value={sensor.ldr} />
        <Card title="Lamp Status" value={sensor.lamp} />
      </div>

      <div className="bg-white rounded-xl shadow p-6 text-center">
        <p className="mb-4 font-semibold">
          Mode: {control.mode}
        </p>

        <div className="flex justify-center gap-3 mb-4">
          <Button onClick={() => setMode("AUTO")} text="AUTO" />
          <Button onClick={() => setMode("MANUAL")} text="MANUAL" />
        </div>

        <div className="flex justify-center gap-3">
          <Button onClick={() => setLamp("ON")} text="ON" />
          <Button onClick={() => setLamp("OFF")} text="OFF" />
        </div>
      </div>
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div className="bg-white p-4 rounded-xl shadow text-center">
      <p className="text-gray-500">{title}</p>
      <p className="text-xl font-bold">{value}</p>
    </div>
  );
}

function Button({ text, onClick }) {
  return (
    <button
      onClick={onClick}
      className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
    >
      {text}
    </button>
  );
}
