using System.Collections.Generic;
namespace LobotomyDatabase.Models
{
	public enum RiskLevel
	{
		ZAYIN,
		TETH,
		HE,
		WAW,
		ALEPH
	}
	public class Abnormality
	{
		public int ID { get; set; }
		public string? in_game_id { get; set; }
		public string? Name { get; set; }
		public string? NumCode { get; set; }
		public RiskLevel? RiskLevel { get; set; }
		public string? OpenText { get; set; }
		public virtual ICollection<AbnormalityStory>? Stories { get; set; }
		public virtual ICollection<AbnormalityTip>? Tips { get; set; }
		public virtual ICollection<AbnormalityNarration>? Narrations { get; set; }
	}
}
