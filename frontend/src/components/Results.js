function Results({ data }) {
  return (
    <div className="max-w-3xl mx-auto py-12 px-6">
      <h2 className="text-3xl font-bold text-dustyOrchid mb-6">
        Results for {data.name}
      </h2>
      <div className="space-y-4">
        {Object.entries(data.skills).map(([skill, value]) => (
          <div key={skill} className="bg-white rounded-lg p-4 shadow-md">
            <div className="flex justify-between mb-2">
              <span className="font-semibold">{skill}</span>
              <span>{value}%</span>
            </div>
            <div className="w-full bg-lilacGrey rounded-full h-3">
              <div
                className="bg-dustyOrchid h-3 rounded-full"
                style={{ width: `${value}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Results;
