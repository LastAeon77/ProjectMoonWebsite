
using LobotomyDatabase.Data;
using Microsoft.AspNetCore.HttpOverrides;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Hosting;
using Newtonsoft.Json;
using System.Text.Json;

namespace LobotomyDatabase
{
	public class Program
	{
		public static void Main(string[] args)
		{
			var builder = WebApplication.CreateBuilder(args);



			// Add services to the container.

			builder.Services.AddControllers();
			// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
			builder.Services.AddDbContext<LobotomyData>(options =>
				options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
			builder.Services.AddEndpointsApiExplorer();
			builder.Services.AddSwaggerGen();
			var app = builder.Build();
			using (var scope = app.Services.CreateScope())
			{
				var db = scope.ServiceProvider.GetRequiredService<LobotomyData>();
				db.Database.Migrate();
			}
			app.UseForwardedHeaders(new ForwardedHeadersOptions
			{
				ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
			});

			// Configure the HTTP request pipeline.

			app.UseSwagger();
			app.UseSwaggerUI();


			// app.UseHttpsRedirection();

			app.UseAuthorization();


			app.MapControllers();

			app.Run();
		}
	}
}