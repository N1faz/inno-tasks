var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello from .NET 8.0!");

app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));

app.Run("http://0.0.0.0:8081");
