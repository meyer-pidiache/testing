using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NumeroMayor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Double numero1 = Convert.ToDouble(numericUpDown1.Value);
            Double numero2 = Convert.ToDouble(numericUpDown2.Value);

            MessageBox.Show($"{numero1} es {((numero1 > numero2) ? "mayor" : "menor")} que {numero2}");
        }
    }
}
