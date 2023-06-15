using LobotomyDatabase.Models;
using Microsoft.EntityFrameworkCore;


namespace LobotomyDatabase.Data
{
	public class LobotomyData :DbContext
	{
		public LobotomyData(DbContextOptions<LobotomyData> options) : base(options)
		{
		}
		public DbSet<Abnormality> Abnormalities { get; set; }
		public DbSet<AbnormalityStory> AbnormalitiesStories { get; set; }
		public DbSet<AbnormalityTip> AbnormalitiesTips { get; set; }
		public DbSet<AbnormalityNarration> AbnormalityNarrations { get; set; }
		protected override void OnModelCreating(ModelBuilder modelBuilder)
		{
			modelBuilder.Entity<Abnormality>().ToTable("Abnormality");
			modelBuilder.Entity<AbnormalityStory>().ToTable("AbnormalityStory");
			modelBuilder.Entity<AbnormalityTip>().ToTable("AbnormalityTip");
			modelBuilder.Entity<AbnormalityNarration>().ToTable("AbnormalityNarration");
		}
	}
}
