using System.ComponentModel.DataAnnotations.Schema;

namespace LobotomyDatabase.Models
{
	public class AbnormalityNarration
	{
		public int ID { get; set; }
		public string? Narration { get; set; }
		public string? NarrationAction { get; set; }

		[ForeignKey("Abnormality")]
		public int? AbnormalityID { get; set; }
		public virtual Abnormality? Abnormality { get; set; }
	}
}
