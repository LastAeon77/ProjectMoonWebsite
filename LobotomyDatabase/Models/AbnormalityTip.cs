using System.ComponentModel.DataAnnotations.Schema;

namespace LobotomyDatabase.Models
{
	public class AbnormalityTip
	{
		public int ID { get; set; }
		public string? Tip { get; set; }
		public string? TipNum { get; set; }
		[ForeignKey("Abnormality")]
		public int? AbnormalityID { get; set; }
		public virtual Abnormality? Abnormality { get; set; }
	}
}
